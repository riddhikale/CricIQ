# 🏏 CricIQ

Cricket Analytics & Prediction Platform

CricIQ is a ML-powered cricket analytics platform that provides real-time predictions for IPL matches, player auction prices, and first innings scores.

Built using Python and deployed on Streamlit Cloud, the app transforms raw cricket data into actionable insights through interactive predictions.

Live App: https://criciq-6imtd47rte9gqxzlyhyeqg.streamlit.app/

---

## Features

### Auction Price Predictor

Predicts a player's IPL auction price using:

- Total Runs
- Batting Average
- Strike Rate
- Total Wickets
- Bowling Economy & Average
- Matches Played

---

### Match Winner Predictor

Predicts match outcome based on:

- Teams
- Toss winner & decision
- Venue
- Season

---

### First Innings Score Predictor

Estimates final score using:

- Powerplay runs (overs 1–6)
- Powerplay wickets
- Match context (teams, venue, season)

---

## Machine Learning Models

- Auction Price Predictor → Regression (Linear, Ridge, Random Forest)
- Match Winner Predictor → Classification (Logistic Regression, Random Forest)
- Score Predictor → Regression (Ridge, Gradient Boosting)

---

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## Project Structure

<pre>
IPL-Analysis/
│
├── app.py
├── requirements.txt
│
├── models/
│   ├── auction_price_model.pkl
│   ├── match_winner_model.pkl
│   ├── innings_score_model.pkl
│   ├── match_columns.pkl
│   └── innings_columns.pkl
│
├── src/
│   └── predict.py
│
└── notebooks/
    ├── 01_eda.ipynb
    ├── 02_ml_auction_price.ipynb
    ├── 03_ml_match_winner.ipynb
    └── 04_ml_innings_score.ipynb
</pre>

---

## How to Run Locally

git clone https://github.com/riddhikale/CricIQ.git

cd CricIQ

pip install -r requirements.txt
streamlit run app.py

---

## Key Highlights

- Built 3 end-to-end ML models using IPL data
- Performed feature engineering from ball-by-ball dataset
- Created an interactive UI for real-time predictions
- Deployed a complete ML application online

---

## Future Improvements

- Add confidence scores
- Improve model accuracy
- Integrate live match data
- Add player comparison dashboard

### ⭐ If you like this project, give it a star!
