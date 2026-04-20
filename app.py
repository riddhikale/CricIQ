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

    if st.button("Predict Price", key="predict_price"):
    
        if (
            total_runs == 0 and
            batting_average == 0 and
            strike_rate == 0 and
            total_wickets == 0 and
            matches_played == 0
        ):
            st.warning("⚠️ Enter player stats to get a meaningful prediction")
            st.stop()

        if matches_played == 0:
            st.warning("⚠️ Player must have played at least 1 match")
            st.stop()

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

    team1 = st.selectbox("Team 1", ["Select Team"] + teams)
    team2 = st.selectbox("Team 2", ["Select Team"] + teams)

    toss_winner = st.selectbox("Toss Winner", ["Select Team", team1, team2])
    toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

    venue = st.selectbox("Venue", venues)
    season = st.number_input("Season", 2008, 2025, value=2025)

    if st.button("Predict Match Winner", key="match_btn"):

        if team1 == "Select Team" or team2 == "Select Team":
            st.warning("⚠️ Please select both teams")
            st.stop()

        if team1 == team2:
            st.error("❌ Teams must be different")
            st.stop()

        if toss_winner == "Select Team":
            st.warning("⚠️ Select toss winner")
            st.stop()

        # ✅ DATA PREP
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




