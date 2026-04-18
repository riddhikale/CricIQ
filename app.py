import streamlit as st
from src.predict import (
    predict_auction_price,
    predict_match_winner,
    predict_innings_score
)

st.title("🏏 CricPredictor")

tab1, tab2, tab3 = st.tabs([
    "💰 Auction Price",
    "🏆 Match Winner",
    "🎯 Score Predictor"
])

with tab1:
    st.header("Auction Price Predictor")

    total_runs = st.number_input("Total Runs", 0)
    batting_average = st.number_input("Batting Average", 0.0)
    strike_rate = st.number_input("Strike Rate", 0.0)
    total_wickets = st.number_input("Total Wickets", 0)
    bowling_economy = st.number_input("Bowling Economy", 0.0)
    bowling_average = st.number_input("Bowling Average", 0.0)
    matches_played = st.number_input("Matches Played", 0)

    if st.button("Predict Price"):
        data = {
            "total_runs": total_runs,
            "batting_average": batting_average,
            "strike_rate": strike_rate,
            "total_wickets": total_wickets,
            "bowling_economy": bowling_economy,
            "bowling_average": bowling_average,
            "matches_played": matches_played
        }

        price = predict_auction_price(data)

        st.success(f"💰 Predicted Price: ₹ {price:,.0f}")

