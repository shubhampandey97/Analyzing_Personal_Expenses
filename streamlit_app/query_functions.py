import pymysql
import pandas as pd
from config import DB_CONFIG

def fetch_data(query):
    conn = pymysql.connect(**DB_CONFIG)
    df = pd.read_sql(query, conn)
    conn.close()
    return df
