import pandas as pd
from sqlalchemy import create_engine
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

def extract():
    engine = get_engine()

    delivery = pd.read_sql_query("SELECT * FROM deliveries;", engine)
    player = pd.read_sql_query("SELECT * FROM player;", engine)
    player_captain = pd.read_sql_query("SELECT * FROM player_captain;", engine)

    return delivery, player, player_captain