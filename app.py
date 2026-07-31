import os
import pickle
from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

from graphs import get_all_graph_data

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"

fund_data = pd.read_pickle(MODEL_DIR / "cleaned_funds.pkl")
fund_data = fund_data.reset_index(drop=True)
fund_data["id"] = fund_data.index

dashboard = {
    "totalFunds": len(fund_data),
    "totalCategories": fund_data["category"].nunique(),
    "totalAMC": fund_data["fund_name"].nunique(),
    "highestFundSize": fund_data["aum"].max(),
    "oldestFund": fund_data["Inception Date"].min(),
    "totalStocks": fund_data["number_of_stocks"].sum()
}

print("Dataset Loaded")

with open(MODEL_DIR / "return_model.pkl", "rb") as file:
    model = pickle.load(file)
print("Model Loaded")

@app.route("/")
def home():
    empty_funds = fund_data.iloc[0:0]

    graph_data = get_all_graph_data()

    return render_template(
        "index.html",
        active_page="home",
        funds=empty_funds,
        fund=None,
        dashboard=dashboard,
        graph_data=graph_data,
        sip=None,
        investment_horizon=None,
        total_investment=0,
        estimated_return=0,
        final_amount=0
    )

@app.route("/search")
def search():
    query = request.args.get("query", "").strip()

    if query:
        searched_funds = fund_data[fund_data["scheme_name"].str.contains(query, case=False, na=False)]
    else:
        searched_funds = fund_data

    graph_data = get_all_graph_data()

    return render_template(
        "index.html",
        active_page="investments",
        dashboard=dashboard,
        funds=searched_funds,
        graph_data=graph_data,
        fund=None,
        sip=None,
        investment_horizon=None,
        total_investment=0,
        estimated_return=0,
        final_amount=0
    )

@app.route("/investments")
def investments():
    graph_data = get_all_graph_data()

    return render_template(
        "index.html",
        active_page="investments",
        dashboard=dashboard,
        funds=fund_data,
        fund=None,
        graph_data=graph_data,
        sip=None,
        investment_horizon=None,
        total_investment=0,
        estimated_return=0,
        final_amount=0
    )

@app.route("/recommend", methods=["GET"])
def recommend_page():
    graph_data = get_all_graph_data()

    return render_template(
        "index.html",
        active_page="recommend",
        dashboard=dashboard,
        funds=fund_data.iloc[0:0],
        fund=None,
        graph_data=graph_data,
        sip=None,
        investment_horizon=None,
        total_investment=0,
        estimated_return=0,
        final_amount=0
    )


@app.route("/recommend", methods=["POST"])
def recommend():
    sip = int(request.form["sip"])
    investment_horizon = request.form["investment_horizon"]
    category = request.form["category"]
    recommended_funds = fund_data.copy()
    if category:
        recommended_funds = recommended_funds[recommended_funds["category"] == category]

    if investment_horizon == "1 Year":
        recommended_funds = recommended_funds.sort_values(by=["rating", "return_1_year"],ascending=False)
    elif investment_horizon == "3 Years":
        recommended_funds = recommended_funds.sort_values(by=["rating", "return_3_year"],ascending=False)
    else:
        recommended_funds = recommended_funds.sort_values(by=["rating", "return_5_year"],ascending=False)

    recommended_funds = recommended_funds.head(12)
    graph_data = get_all_graph_data()

    return render_template(
        "index.html",
        dashboard=dashboard,
        active_page="results",
        funds=recommended_funds,
        fund=None,
        graph_data=graph_data,
        sip=sip,
        investment_horizon=investment_horizon,
        total_investment=0,
        estimated_return=0,
        final_amount=0
    )


@app.route("/details/<int:fund_id>")
def details(fund_id):
    source = request.args.get("source")
    sip = request.args.get("sip")
    investment_horizon = request.args.get("year")
    selected_fund = fund_data[fund_data["id"] == fund_id].iloc[0]
    graph_data = get_all_graph_data()

    fund_graph = {
        "labels": ['1 Year', '3 Years', '5 Years'],
        "values": [selected_fund['return_1_year'], selected_fund['return_3_year'], selected_fund['return_5_year']]
    }
       
    return render_template(
        "index.html",
        dashboard=dashboard,
        active_page="funds",
        funds=fund_data.iloc[0:0],
        fund=selected_fund,
        graph_data=graph_data,
        fund_graph=fund_graph,
        source=source,
        sip=sip,
        investment_horizon=investment_horizon,
        total_investment=0,
        estimated_return=0,
        final_amount=0
    )


@app.route("/predict/<int:fund_id>")
def predict(fund_id):
    sip = request.args.get("sip")
    if sip is None:
        return "SIP value is missing."
    sip = int(sip)
    
    investment_horizon = request.args.get("year")
    selected_fund = fund_data[fund_data["id"] == fund_id].iloc[0]
    expense_ratio = selected_fund["expense_ratio"]
    monthly_expense = (sip * expense_ratio) / 100
    annual_expense = monthly_expense * 12

    if investment_horizon == "1 Year":
        years = 1
    elif investment_horizon == "3 Years":
        years = 3
    else:
        years = 5

    total_investment = sip * 12 * years
    total_expense = annual_expense * years

    input_data = pd.DataFrame({
        "nav": [selected_fund["nav"]],
        "aum": [selected_fund["aum"]],
        "expense_ratio": [selected_fund["expense_ratio"]],
        "large_cap": [selected_fund["large_cap"]],
        "mid_cap": [selected_fund["mid_cap"]],
        "small_cap": [selected_fund["small_cap"]],
        "average_market_cap": [selected_fund["average_market_cap"]],
        "standard_deviation": [selected_fund["standard_deviation"]],
        "category_average_return": [selected_fund["category_average_return"]]
    })

    prediction = model.predict(input_data)
    return_1 = prediction[0][0]
    return_3 = prediction[0][1]
    return_5 = prediction[0][2]

    if investment_horizon == "1 Year":
        predicted_percent = return_1
    elif investment_horizon == "3 Years":
        predicted_percent = return_3
    else:
        predicted_percent = return_5

    estimated_return = total_investment * predicted_percent / 100
    final_amount = total_investment + estimated_return

    if estimated_return > 5:
        sentiment = "Positive"
    elif estimated_return < 5 and estimated_return > 0:
        sentiment = "Neutral"
    elif estimated_return < 0:
        sentiment = "Negative"

    graph_data = get_all_graph_data()

    return render_template(
        "index.html",
        dashboard=dashboard,
        active_page="predict",
        funds=fund_data.iloc[0:0],
        fund=selected_fund,
        graph_data=graph_data,
        sip=sip,
        investment_horizon=investment_horizon,
        total_investment=total_investment,
        estimated_return=estimated_return,
        final_amount=final_amount,
        sentiment=sentiment,
        monthly_expense=monthly_expense,
        annual_expense=annual_expense,
        total_expense=total_expense,
        predicted_return_1_year=return_1,
        predicted_return_3_year=return_3,
        predicted_return_5_year=return_5
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
