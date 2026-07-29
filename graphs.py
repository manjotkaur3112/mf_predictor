import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_pickle("model/cleaned_funds.pkl")

def average_returns_chart():

    average_returns = {
        "1 Year": df["return_1_year"].mean(),
        "3 Years": df["return_3_year"].mean(),
        "5 Years": df["return_5_year"].mean()
    }

    plt.figure(figsize=(5,3))

    plt.plot(list(average_returns.keys()),list(average_returns.values()),marker="o",linewidth=3)

    plt.title("Average Returns")
    plt.xlabel("Investment Period")
    plt.ylabel("Average Return (%)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("static/average_returns.png")
    plt.close()


def expense_ratio_chart():

    plt.figure(figsize=(5,4))

    plt.hist(
        df["expense_ratio"],
        bins=20,
        edgecolor="black"
    )

    plt.title("Expense Ratio Distribution")
    plt.xlabel("Expense Ratio (%)")
    plt.ylabel("Number of Funds")
    plt.grid(axis="y")

    plt.tight_layout()
    plt.savefig("static/expense_ratio.png")
    plt.close()


def risk_return_chart():

    plt.figure(figsize=(5,3))

    plt.scatter(
        df["standard_deviation"],
        df["return_5_year"],
        alpha=0.7
    )

    plt.title("Risk vs Return")
    plt.xlabel("Risk (Standard Deviation)")
    plt.ylabel("5-Year Return (%)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("static/risk_return.png")
    plt.close()

def classification_chart():
    df = pd.read_csv("data/mutual_funds.csv")
    
    df["Main_Classification"] = (df["classification"].str.split(":").str[0].str.strip())

    main_classification = df["Main_Classification"].value_counts()

    plt.figure(figsize=(5,4))

    main_classification.plot(kind="bar",color=["royalblue", "orange", "green", "red"],edgecolor="black")

    plt.title("Distribution of Mutual Funds by Main Classification")
    plt.xlabel("Main Classification")
    plt.ylabel("Number of Mutual Funds")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for i, value in enumerate(main_classification):
        plt.text(i, value + 2, str(value), ha="center")

    plt.tight_layout()
    plt.savefig("static/classification_chart.png")
    plt.close()

def generate_all_graphs():
    average_returns_chart()
    expense_ratio_chart()
    risk_return_chart()
    classification_chart()