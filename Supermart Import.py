# === Imports ===
import pandas as pd
import psycopg2
import pymysql
from sqlalchemy import create_engine

# === Load CSV ===
df = pd.read_csv("Supermart.csv")

# -------------------------------
# PostgreSQL Section
# -------------------------------
pg_user = "postgres"      # your Postgres username
pg_pass = "root"          # your Postgres password
pg_host = "localhost"
pg_port = "5432"
pg_db = "supermart"

# Step 1: Connect to default postgres database
try:
    pg_conn = psycopg2.connect(
        dbname="postgres",
        user=pg_user,
        password=pg_pass,
        host=pg_host,
        port=pg_port
    )
    pg_conn.autocommit = True
    pg_cursor = pg_conn.cursor()

    # Step 2: Create database if not exists
    pg_cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{pg_db}'")
    exists = pg_cursor.fetchone()
    if not exists:
        pg_cursor.execute(f"CREATE DATABASE {pg_db}")
        print("PostgreSQL database 'supermart' created.")
    else:
        print("ℹPostgreSQL database 'supermart' already exists.")

    pg_cursor.close()
    pg_conn.close()

    # Step 3: Push data to PostgreSQL
    pg_engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")
    df.to_sql("supermart", pg_engine, if_exists="replace", index=False)
    print("Supermart data successfully loaded into PostgreSQL!")

except Exception as e:
    print("Error with PostgreSQL:", e)

# -------------------------------
# MySQL Section
# -------------------------------
mysql_user = "root"       # your MySQL username
mysql_pass = "root"       # your MySQL password
mysql_host = "localhost"
mysql_port = 3306
mysql_db = "supermart"

try:
    # Step 1: Connect to MySQL default server
    mysql_conn = pymysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_pass,
        port=mysql_port
    )
    mysql_conn.autocommit(True)
    mysql_cursor = mysql_conn.cursor()

    # Step 2: Create database if not exists
    mysql_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_db}")
    print("MySQL database 'supermart' ensured.")

    mysql_cursor.close()
    mysql_conn.close()

    # Step 3: Push data to MySQL
    mysql_engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_db}")
    df.to_sql("supermart", mysql_engine, if_exists="replace", index=False)
    print("Supermart data successfully loaded into MySQL!")

except Exception as e:
    print("Error with MySQL:", e)

# -------------------------------
# Final Verification
# -------------------------------
print("\n=== Verification ===")
print("Shape of DataFrame:", df.shape)
print("Columns:", list(df.columns))
print("First 5 rows:\n", df.head())
