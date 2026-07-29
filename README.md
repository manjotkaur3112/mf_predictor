# 📈 Mutual Fund Recommendation & Return Prediction System

A Machine Learning-based web application developed using **Python**, **Flask**, and **Scikit-learn** that recommends suitable mutual funds and predicts expected returns based on historical mutual fund data. The application also includes sentiment analysis and interactive graphical visualizations to help users make informed investment decisions.

---

## 📌 Project Overview

Choosing the right mutual fund among hundreds of available schemes can be challenging, especially for beginner investors. This project simplifies the investment process by analyzing mutual fund data and providing personalized recommendations based on user inputs.

The system uses a **Random Forest Regression** model trained on historical mutual fund data to estimate expected returns. A Flask-based web interface allows users to interact with the system easily.

---

## 🚀 Features

- ✔ Mutual Fund Recommendation
- ✔ Return Prediction using Machine Learning
- ✔ Sentiment Analysis
- ✔ Interactive Dashboard
- ✔ Category-wise Fund Filtering
- ✔ Fund Detail Page
- ✔ Performance Graphs
- ✔ Expense Ratio Analysis
- ✔ Category Distribution Graph
- ✔ Return Comparison Graph
- ✔ Responsive User Interface

---

## 🛠 Technologies Used

### Programming Language

- Python 3.x

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- JavaScript

### Machine Learning

- Scikit-learn
- Random Forest Regressor

### Data Processing

- Pandas

### Data Visualization

- Matplotlib

### Model Storage

- Pickle

---

# 📂 Project Structure

```
Mutual_Fund_Predictor/
│
├── app.py
├── train_model.py
├── graphs.py
├── requirements.txt
├── README.md
│
├── data/
│     └── mutual_funds.csv
│
├── model/
│     ├── return_model.pkl
│     ├── cleaned_funds.pkl
│
├── static/
│     ├── style.css
│     └── graphs.png
│
├── templates/
│     ├── index.html
```

---

# 📊 Dataset

The project uses a CSV dataset containing historical information about mutual funds.

### Dataset Attributes

- Fund Name
- Scheme Name
- Category
- Rating
- NAV
- Assets Under Management (AUM)
- Expense Ratio
- Large Cap %
- Mid Cap %
- Small Cap %
- 1 Year Return
- 3 Year Return
- 5 Year Return
- Fund Classification

---

# ⚙ Machine Learning Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Feature Selection
   │
   ▼
Train-Test Split
   │
   ▼
Random Forest Regression
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
   │
   ▼
Flask Web Application
```

---

# 📈 Model Used

**Random Forest Regressor**

Reasons for selecting Random Forest:

- High prediction accuracy
- Handles non-linear relationships
- Reduces overfitting
- Works well with structured tabular data

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/manjotkaur3112/mutual-fund-predictor.git
```

Move into project folder

```bash
cd mutual-fund-predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train Machine Learning Model

If the model files are not already available, run:

```bash
python train_model.py
```

This will generate:

- return_model.pkl
- cleaned_funds.pkl
- processed dataset

---

## Run Flask Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 🖥 Application Workflow

1. Open Website
2. Click Recommend Funds
3. Enter Investment Details
4. Submit Form
5. System Filters Mutual Funds
6. Machine Learning Predicts Returns
7. Best Matching Funds are Displayed
8. User Can View Detailed Analysis
9. Dashboard Displays Graphical Insights

---

# 📊 Generated Graphs

The dashboard includes:

- Average Returns Graph
- Expense Ratio Comparison
- Category Distribution
- Predicted Return Chart
- Fund Performance Graph
- Risk Classification Graph

---

# 🔍 Sentiment Analysis

The project performs sentiment analysis on mutual fund information to classify investment sentiment.

Possible Results:

- Positive
- Neutral
- Negative

---

# ✅ Advantages

- Easy to use
- Fast prediction
- Accurate recommendations
- Interactive dashboard
- Graphical representation
- Beginner friendly
- Machine Learning based

---

# ⚠ Limitations

- Uses historical data
- No live stock market integration
- Limited dataset
- Internet data is not fetched in real time

---

# 👩‍💻 Author

**Manjot Kaur**

B.Tech Computer Science & Engineering (Generative AI)

Lovely Professional University, Jalandhar, Punjab

---

# 📄 License

This project is developed for educational and academic purposes.

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.