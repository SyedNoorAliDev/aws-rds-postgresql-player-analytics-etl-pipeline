def score_board(row):
    score = 0
    score = score + row["runs"] + row["fours"] + 2 * row["sixes"]

    if row["runs"] >= 100:
        score += 16
    elif row["runs"] >= 50:
        score += 8
    elif row["runs"] >= 30:
        score += 4
    elif row["runs"] == 0:
        score -= 2

    if row["balls"] >= 10:
        if row["strike_rate"] > 170:
            score += 6
        elif row["strike_rate"] > 150:
            score += 4
        elif row["strike_rate"] > 130:
            score += 2
        elif row["strike_rate"] > 60 and row["strike_rate"] <= 70:
            score -= 2
        elif row["strike_rate"] > 50 and row["strike_rate"] <= 60:
            score -= 4
        elif row["strike_rate"] <= 50:
            score -= 6

    if row["is_captain"] == 1:
        score = score * 2

    return score


def transform(delivery, player, player_captain):
    temp_df = player.merge(
        player_captain,
        on="player_id"
    )[["player_name", "match_id", "is_captain"]]

    delivery = delivery.merge(
        temp_df,
        left_on=["match_id", "batter"],
        right_on=["match_id", "player_name"],
        how="left"
    ).fillna(0)

    runs = delivery.groupby(["match_id", "batter"])["batsman_runs"].sum().reset_index()

    balls = delivery.groupby(["match_id", "batter"])["batsman_runs"].count().reset_index()

    fours = delivery.query("batsman_runs == 4") \
        .groupby(["match_id", "batter"])["batsman_runs"] \
        .count() \
        .reset_index()

    sixes = delivery.query("batsman_runs == 6") \
        .groupby(["match_id", "batter"])["batsman_runs"] \
        .count() \
        .reset_index()

    final_df = runs.merge(
        balls,
        on=["match_id", "batter"],
        suffixes=["_runs", "_balls"]
    ).merge(
        fours,
        on=["match_id", "batter"],
        how="left"
    ).merge(
        sixes,
        on=["match_id", "batter"],
        how="left"
    )

    final_df.fillna(0, inplace=True)

    final_df.rename(columns={
        "batsman_runs_runs": "runs",
        "batsman_runs_balls": "balls",
        "batsman_runs_x": "fours",
        "batsman_runs_y": "sixes"
    }, inplace=True)

    final_df["strike_rate"] = round((final_df["runs"] / final_df["balls"]) * 100, 2)

    final_df = final_df.merge(
        temp_df,
        left_on=["match_id", "batter"],
        right_on=["match_id", "player_name"],
        how="left"
    ).drop(columns=["player_name"]).fillna(0)

    final_df["score"] = final_df.apply(score_board, axis=1)

    export_df = final_df[
        [
            "match_id",
            "batter",
            "runs",
            "balls",
            "fours",
            "sixes",
            "strike_rate",
            "is_captain",
            "score"
        ]
    ].sort_values(by="score", ascending=False)

    return export_df