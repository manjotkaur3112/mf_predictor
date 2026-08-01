from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"
DATA_DIR = BASE_DIR / "data"


def _load_fund_data():
    df = pd.read_pickle(MODEL_DIR / "cleaned_funds.pkl")
    df = df.reset_index(drop=True)

    numeric_columns = [
        "aum",
        "number_of_stocks",
        "expense_ratio",
        "nav",
        "large_cap",
        "mid_cap",
        "small_cap",
        "average_market_cap",
        "standard_deviation",
        "category_average_return",
        "return_1_year",
        "return_3_year",
        "return_5_year",
    ]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    text_columns = ["fund_name", "scheme_name", "category", "inception_date"]
    for column in text_columns:
        if column in df.columns:
            df[column] = df[column].fillna("").astype(str)

    return df


df = _load_fund_data()
df.to_csv(MODEL_DIR / "cleaned_funds.csv", index=False)

def get_average_returns():
    values = [
        round(df["return_1_year"].mean(), 2),
        round(df["return_3_year"].mean(), 2),
        round(df["return_5_year"].mean(), 2),
    ]

    return {"labels": ["1 Year", "3 Years", "5 Years"], "values": values}


def get_expense_ratio():
    series = pd.to_numeric(df["expense_ratio"], errors="coerce").dropna()
    if series.empty:
        return {"labels": [], "values": []}

    bins = pd.cut(series, bins=10)
    counts = bins.value_counts(sort=False).reindex(bins.cat.categories, fill_value=0)
    labels = [f"{round(i.left, 2)}-{round(i.right, 2)}" for i in bins.cat.categories]

    return {"labels": labels, "values": counts.tolist()}


def get_risk_return():
    x = pd.to_numeric(df["standard_deviation"], errors="coerce").fillna(0).tolist()
    y = pd.to_numeric(df["return_5_year"], errors="coerce").fillna(0).tolist()

    return {"x": x, "y": y}


def get_classification():
    data = pd.read_csv(DATA_DIR / "mutual_funds.csv")
    data["Main"] = data["classification"].fillna("").astype(str).str.split(":").str[0].str.strip()
    data["Main"] = data["Main"].replace("", "Unclassified")

    counts = data["Main"].value_counts().sort_index()

    return {"labels": counts.index.tolist(), "values": counts.values.tolist()}


def get_all_graph_data():
    return {
        "average_returns": get_average_returns(),
        "expense_ratio": get_expense_ratio(),
        "risk_return": get_risk_return(),
        "classification": get_classification(),
    }
