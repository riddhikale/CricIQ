import joblib
import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

auction_path = os.path.join(BASE_DIR, "models", "auction_price_model.pkl")
match_path = os.path.join(BASE_DIR, "models", "match_winner_model.pkl")
innings_path = os.path.join(BASE_DIR, "models", "innings_score_model.pkl")

#load models
auction_model = joblib.load(auction_path)
match_model = joblib.load(match_path)
innings_model = joblib.load(innings_path)


def predict_auction_price(data: dict):
    "Predict auction price from player stats"
    
    df = pd.DataFrame([data])
    prediction = auction_model.predict(df)[0]

    return prediction


def predict_match_winner(data: dict):
    "Predict match winner (1 = team1, 0 = team2)"

    df = pd.DataFrame([data])
    prediction = match_model.predict(df)[0]

    return prediction


def predict_innings_score(data: dict):
    "Predict final innings score from powerplay data"

    df = pd.DataFrame([data])
    prediction = innings_model.predict(df)[0]

    return prediction


#testing
if __name__ == "__main__":
    test_player = {
        "total_runs":2000,
        "batting_average":35,
        "strike_rate":140,
        "total_wickets":10,
        "bowling_economy":8,
        "bowling_average":25,
        "matches_played":80
    }

    print(predict_auction_price(test_player))