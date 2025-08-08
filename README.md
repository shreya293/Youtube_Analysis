# 📊 YouTube Revenue Predictor – ML + Flask Project

This project predicts the estimated revenue (USD) of a YouTube video using basic input parameters such as views, likes, shares, comments, and subscribers.

## 🚀 Features

- Machine Learning model (Random Forest Regressor)
- Clean and simple Flask web interface
- Real-time prediction with user inputs
- Lightweight and easy to run locally

## 🧠 Input Parameters

- Views
- Subscribers
- Likes
- Shares
- Comments

The app also calculates an additional feature internally:

- **Engagement Rate** = (Likes + Shares + Comments) / Views × 100

## 💡 How it works

The model was trained using YouTube channel data. It calculates "Engagement Rate" and uses ML to predict revenue based on user input.

## 🛠️ Tech Stack

- Python
- Jupyter Notebook
- Flask
- HTML/CSS
- scikit-learn
- NumPy, pandas

## 📂 Folder Structure

Youtube_Analysis/
│
├── app.py
├── youtube_revenue_predictor.pkl
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html


## ▶️ How to Run

```bash
git clone https://github.com/yourusername/Youtube_Analysis.git
cd Youtube_Analysis
pip install -r requirements.txt
python app.py

## 📌 Conclusion
The YouTube Revenue Predictor estimates video revenue by analyzing six key performance metrics:

Views

Subscribers

Likes

Shares

Comments

Engagement Rate

These inputs are passed to a trained Random Forest Regression model which identifies patterns from historical data. The model captures how different levels of engagement and visibility typically influence ad earnings.

🎯 In simple words: The more views and interaction a video gets, the higher its chances of earning more — and your model predicts that amount by learning from real YouTube data.
