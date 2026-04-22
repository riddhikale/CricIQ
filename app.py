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
    st.header("💰 Auction Price Predictor")

    col1, col2 = st.columns(2)

    with col1:
        total_runs = st.number_input("Total Runs", 0)
        batting_average = st.number_input("Batting Average", 0.0)
        strike_rate = st.number_input("Strike Rate", 0.0)

    with col2:
        total_wickets = st.number_input("Total Wickets", 0)
        bowling_economy = st.number_input("Bowling Economy", 0.0)
        bowling_average = st.number_input("Bowling Average", 0.0)

    matches_played = st.number_input("Matches Played", 0)

    st.markdown("")

    if st.button("🚀 Predict Auction Price", key="auction_btn"):

        if matches_played == 0:
            st.warning("⚠️ Enter valid player stats")
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

        st.metric("💰 Estimated Price", f"₹ {price/10000000:.2f} Cr")




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




with tab3:
    st.header("First Innings Score Predictor")
    st.caption("Predict final score using powerplay performance and match conditions")

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

    team1 = st.selectbox("Batting Team", ["Select Team"] + teams, key="score_team1")
    team2 = st.selectbox("Bowling Team", ["Select Team"] + teams, key="score_team2")

    venue = st.selectbox("Venue", venues, key="score_venue")
    season = st.number_input("Season", min_value=2008, max_value=2025, value=2025, key="score_season")

    powerplay_runs = st.number_input("Powerplay Runs (Overs 1 to 6)", 0, key="score_runs")
    powerplay_wickets = st.number_input("Powerplay Wickets", 0, key="score_wickets")

    if st.button("Predict Score", key="predict_score"):

        if team1 == "Select Team" or team2 == "Select Team":
            st.warning("⚠️ Please select both teams")
            st.stop()

        if team1 == team2:
            st.error("❌ Teams must be different")
            st.stop()

        if powerplay_runs == 0:
            st.warning("⚠️ Enter realistic powerplay runs")
            st.stop()

        data = {
            "powerplay_runs": powerplay_runs,
            "powerplay_wickets": powerplay_wickets,
            f"team1_{team1}": 1,
            f"team2_{team2}": 1,
            f"venue_{venue}": 1,
            "season": season
        }

        score = predict_innings_score(data)

        st.success(f"🎯 Predicted Score: {int(score)} runs")