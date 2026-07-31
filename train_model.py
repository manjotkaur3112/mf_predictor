import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("data/mutual_funds.csv") 
data = data.rename(
        columns={
            "Fund House": "fund_name",
            "Funds": "scheme_name",
            "Category": "category",
            "Rating": "rating",
            "AUM(in Rs. cr)": "aum",
            "ExpenseRatio (%)": "expense_ratio",
            "Inception": "inception_date",
            "NAV": "nav",
            "52 WeekHigh (NAV)": "high_52_week",
            "52 WeekLow (NAV)": "low_52_week",
            "Return (%)1 mo": "return_1_month",
            "Return (%)1 yr": "return_1_year",
            "Return (%)3 yrs": "return_3_year",
            "Return (%)5 yrs": "return_5_year",
            "No. of Stocks": "number_of_stocks",
            "Large Cap(%)": "large_cap",
            "Mid Cap(%)": "mid_cap",
            "Small Cap(%)": "small_cap",
            "Avg. Market Cap(in Rs. cr)": "average_market_cap",
            "Standard Deviation": "standard_deviation",
            "classification": "classification",
            "category_average_return_1year": "category_average_return",
            "Exit_load_Remarks": "exit_load_remarks"
        }
    )

print("Columns renamed successfully.")
print(data.head())


data = data.dropna()
print("Missing values removed successfully.")

numeric_columns = ["rating","aum","expense_ratio","nav","high_52_week","low_52_week","return_1_month","return_1_year","return_3_year","return_5_year",
        "number_of_stocks","large_cap","mid_cap","small_cap","average_market_cap","standard_deviation","category_average_return"
]


for column in numeric_columns:
    data[column] = pd.to_numeric(data[column],errors="coerce")

data = data.dropna()
print("Numeric columns converted successfully")

def recommend():
    print("Dataset Loaded Successfully")
    print(data.head())
    for column in data.columns:
        print(column)

    data.to_pickle("model/cleaned_funds.pkl")
    print("Cleaned dataset saved successfully.")

    X = data[["nav","aum","expense_ratio","large_cap","mid_cap","small_cap","average_market_cap","standard_deviation","category_average_return"]]

    Y = data[["return_1_year","return_3_year","return_5_year"]]
    print(Y.head())
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("Dataset divided successfully")

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train,Y_train)
    pickle.dump(model, open("model/return_model.pkl", "wb"))
    print("Model trained successfully.")

recommend()