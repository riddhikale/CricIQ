import streamlit as st
from src.predict import (
    predict_auction_price,
    predict_match_winner,
    predict_innings_score
)

st.set_page_config(page_title="CricIQ", layout="wide")


st.title("🏏CricIQ")

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


tab1, tab2, tab3 = st.tabs([
    "💰 Auction Price",
    "🏆 Match Winner",
    "🎯 First Innings Score"
])




with tab1:
    st.caption("Predict player's auction price based on stats, role and performance history")

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
    st.caption("Predict match outcome based on teams, toss, and venue")

    col1, col2 = st.columns(2)

    with col1:
        team1 = st.selectbox("Team 1", ["Select Team"] + teams)
        toss_winner = st.selectbox("Toss Winner", ["Select Team", team1, team2 if 'team2' in locals() else ""])

    with col2:
        team2 = st.selectbox("Team 2", ["Select Team"] + teams)
        toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

    venue = st.selectbox("Venue", ["Select Venue"] + venues)
    season = st.number_input("📅 Season", 2008, 2025, value=2025)

    if st.button("🚀 Predict Winner", key="match_btn"):

        if team1 == "Select Team" or team2 == "Select Team":
            st.warning("⚠️ Please select both teams")
            st.stop()

        if team1 == team2:
            st.error("❌ Teams must be different")
            st.stop()

        if toss_winner == "Select Team":
            st.warning("⚠️ Select toss winner")
            st.stop()

        data = {
            f"team1_{team1}": 1,
            f"team2_{team2}": 1,
            f"toss_winner_{toss_winner}": 1,
            f"toss_decision_{toss_decision}": 1,
            f"venue_{venue}": 1,
            "season": season
        }

        result = predict_match_winner(data)

        winner = team1 if result == 1 else team2

        st.metric("🏆 Predicted Winner", winner)



with tab3:
    st.caption("Predict final score using powerplay performance and match conditions")

    col1, col2 = st.columns(2)

    with col1:
        team1 = st.selectbox("Batting Team", ["Select Team"] + teams, key="score_team1")
        powerplay_runs = st.number_input("Powerplay Runs (Overs 1–6)", 0, key="score_runs")

    with col2:
        team2 = st.selectbox("Bowling Team", ["Select Team"] + teams, key="score_team2")
        powerplay_wickets = st.number_input("Powerplay Wickets", 0, key="score_wickets")

    venue = st.selectbox("Venue", ["Select Venue"] + venues, key="score_venue")
    season = st.number_input("Season", 2008, 2025, value=2025, key="score_season")


    if st.button("⚡ Predict Score", key="predict_score"):

        if team1 == "Select Team" or team2 == "Select Team":
            st.warning("⚠️ Please select both teams")
            st.stop()

        if team1 == team2:
            st.error("❌ Teams must be different")
            st.stop()

        if venue == "Select Venue":
            st.warning("⚠️ Please select venue")
            st.stop()

        if powerplay_runs == 0:
            st.warning("⚠️ Powerplay runs must be greater than 0")
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

        if score is None:
            st.error("⚠️ Prediction failed. Check model input.")
        else:
            st.metric("🎯 Predicted Score", f"{int(score)} runs")


