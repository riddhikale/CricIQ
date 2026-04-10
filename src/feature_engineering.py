import pandas as pd

#batting stats
def compute_batting_stats(deliveries):

    player_runs = deliveries.groupby("batter")["batsman_runs"].sum()

    balls_faced = deliveries.groupby("batter").size()

    dismissals = deliveries[deliveries["is_wicket"] == 1] \
        .groupby("player_dismissed").size()

    batting_stats = pd.DataFrame({
        "total_runs": player_runs,
        "balls_faced": balls_faced
    })

    batting_stats["dismissals"] = dismissals

    batting_stats.fillna(0, inplace=True)

    batting_stats["batting_average"] = (
        batting_stats["total_runs"] / batting_stats["dismissals"].replace(0,1)
    )

    batting_stats["strike_rate"] = (
        batting_stats["total_runs"] / batting_stats["balls_faced"]
    ) * 100

    return batting_stats


#bowling stats
def compute_bowling_stats(deliveries):

    wickets = deliveries.groupby("bowler")["is_wicket"].sum()

    runs_conceded = deliveries.groupby("bowler")["total_runs"].sum()

    balls_bowled = deliveries.groupby("bowler").size()

    bowling_stats = pd.DataFrame({
        "total_wickets": wickets,
        "runs_conceded": runs_conceded,
        "balls_bowled": balls_bowled
    })

    bowling_stats["overs"] = bowling_stats["balls_bowled"] / 6

    bowling_stats["bowling_economy"] = (
        bowling_stats["runs_conceded"] / bowling_stats["overs"]
    )

    bowling_stats["bowling_average"] = (
        bowling_stats["runs_conceded"] / bowling_stats["total_wickets"].replace(0,1)
    )

    return bowling_stats



#matches played
def compute_matches_played(deliveries):
    """
    Calculate number of matches played by each player
    """

    matches_played = deliveries.groupby("batter")["match_id"].nunique()

    matches_played = matches_played.reset_index()

    matches_played.rename(columns={
        "batter": "player",
        "match_id": "matches_played"
    }, inplace=True)

    return matches_played