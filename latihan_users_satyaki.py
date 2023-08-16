import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def load(file, table_name):
    # read csv
    data = pd.read_csv(file, encoding='unicode_escape')

    user = 'postgres'
    passwd = 'postgres'
    hostname = 'localhost'
    database = 'postgres'

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5433/{database}'

    db = create_engine(conn_string)
    conn = db.connect()

    data.to_sql(table_name, con=conn, if_exists='append',
                index=False)

    # conn = psycopg2.connect(conn_string)

if __name__ == '__main__':
    load('D:\VSCode\Project3\python-postgresql/global_youtube_stat.csv', 'latihan_users_satyaki')
