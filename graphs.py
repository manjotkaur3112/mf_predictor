import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df = pd.read_pickle(
    os.path.join(BASE_DIR, "model", "cleaned_funds.pkl")
)

data = pd.read_csv(
    os.path.join(BASE_DIR, "data", "mutual_funds.csv")
)

def get_average_returns():

    return {
        "labels": ["1 Year", "3 Years", "5 Years"],
        "values": [
            round(df["return_1_year"].mean(),2),
            round(df["return_3_year"].mean(),2),
            round(df["return_5_year"].mean(),2)
        ]
    }


def get_expense_ratio():

    counts, bins = pd.cut(df["expense_ratio"],bins=10).value_counts(sort=False), pd.cut(df["expense_ratio"], bins=10).cat.categories

    labels = [f"{round(i.left,2)}-{round(i.right,2)}" for i in bins]

    return {
        "labels": labels,
        "values": counts.tolist()
    }


def get_risk_return():

    return {
        "x": df["standard_deviation"].fillna(0).tolist(),
        "y": df["return_5_year"].fillna(0).tolist()
    }


def get_classification():
    data["Main"] = (data["classification"].str.split(":").str[0].str.strip())

    counts = data["Main"].value_counts()

    return {
        "labels": counts.index.tolist(),
        "values": counts.values.tolist()
    }

def get_all_graph_data():

    return {
        "average_returns":get_average_returns(),
        "expense_ratio":get_expense_ratio(),
        "risk_return":get_risk_return(),
        "classification":get_classification()
    }
