from extract import get_engine

def load(df):
    engine = get_engine()

    df.to_sql(
        name="player_match_stats",
        con=engine,
        schema="analytics",
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into analytics.player_match_stats")