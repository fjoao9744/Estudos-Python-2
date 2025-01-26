import psycopg2
import os

postgre_password = os.getenv("POSTGRE_PASSWORD")
postgre_port = os.getenv("POSTGRE_PORT")

conn = psycopg2.connect(
    database="database.py",
    user="fjoao",
    host="localhost",
    password=postgre_password,
    port=postgre_port
)

conn.close()