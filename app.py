import streamlit as st
from src.predict import (
    predict_auction_price,
    predict_match_winner,
    predict_innings_score
)

st.set_page_config(page_title="CricPredictor", layout="wide")

st.title("🏏 CricPredictor")

tab1, tab2, tab3 = st.tabs([
    "💰 Auction Price",
    "🏆 Match Winner",
    "🎯 Score Predictor"
])



with tab1:
    st.header("Auction Price Predictor")
    st.caption("Predict player's auction price based on stats, role and performance history")

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

        st.success(f"💰 Predicted Price: ₹ {price:,.0f} ({price/10000000:.2f} Cr)")




with tab2:
    st.header("Match Winner Predictor")
    st.caption("Predict match outcome based on teams, toss, and venue")

    teams = [
        "Mumbai Indians",
        "Chennai Super Kings",
        "Royal Challengers Bengaluru",
        "Kolkata Knight Riders",
        "Delhi Capitals",
        "Punjab Kings",
        "Rajasthan Royals",
        "Sunrisers Hyderabad",
        "Gujarat Titans",
        "Lucknow Super Giants"
    ]

    venues = [
        "Wankhede Stadium",
        "Eden Gardens",
        "M Chinnaswamy Stadium",
        "MA Chidambaram Stadium",
        "Arun Jaitley Stadium",
        "Narendra Modi Stadium",
        "Sawai Mansingh Stadium",
        "Rajiv Gandhi International Stadium",
        "Punjab Cricket Association Stadium"
    ]

    team1 = st.selectbox("Team 1", teams)
    team2 = st.selectbox("Team 2", teams, index=1)

    if team1 == team2:
        st.error("Teams must be different")
        st.stop()

    toss_winner = st.selectbox("Toss Winner", [team1, team2])
    toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

    venue = st.selectbox("Venue", venues)

    season = st.number_input("Season", min_value=2008, max_value=2025, value=2025)

    if st.button("Predict Match Winner"):

        data = {
            f"team1_{team1}": 1,
            f"team2_{team2}": 1,
            f"toss_winner_{toss_winner}": 1,
            f"toss_decision_{toss_decision}": 1,
            f"venue_{venue}": 1,
            "season": season
        }

        result = predict_match_winner(data)

        if result == 1:
            st.success(f"🏆 {team1} is likely to win")
        else:
            st.success(f"🏆 {team2} is likely to win")


