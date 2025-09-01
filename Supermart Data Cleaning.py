# Step 1 - Data Exploration and Loading

# Import dependencies
import pandas as pd
import pymysql  # MySQL adapter
from sqlalchemy import create_engine
import psycopg2

# Load CSV
df = pd.read_csv('Supermart.csv', encoding_errors='ignore')

# Basic info
print(df.shape)
print(df.head())
print(df.describe())
print(df.info())

# Handle duplicates
print("Duplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("After dropping duplicates:", df.duplicated().sum())

# Handle missing values
print("Missing values:\n", df.isnull().sum())
df.dropna(inplace=True)
print("After dropping missing values:\n", df.isnull().sum())
print(df.shape)

# -----------------------------
# Step 2 - Column Type Fix
# -----------------------------
# Remove $ and convert to float
df['unit_price'] = df['unit_price'].replace('[\$,]', '', regex=True).astype(float)
df['quantity'] = df['quantity'].astype(float)

# Calculate total sales
df['total'] = df['unit_price'] * df['quantity']

# Standardize column names
df.columns = df.columns.str.lower()
print(df.columns)

# -----------------------------
# Step 3 - Save Cleaned CSV
# -----------------------------
df.to_csv('Supermart_clean_data.csv', index=False)

# -----------------------------
# Step 4 - Database Connections
# -----------------------------

# MySQL connection
engine_mysql = create_engine("mysql+pymysql://root@localhost:3306/Supermart")

try:
    with engine_mysql.connect() as conn:
        print("Connected to MySQL successfully")
except Exception as e:
    print("MySQL connection failed:", e)

# Upload to MySQL
df.to_sql(name='supermart', con=engine_mysql, if_exists='append', index=False)
print("Data uploaded to MySQL")

# PostgreSQL connection
engine_psql = create_engine("postgresql+psycopg2://postgres:x0000@localhost:5432/Supermart")

try:
    with engine_psql.connect() as conn:
        print("Connected to PostgreSQL successfully")
except Exception as e:
    print("PostgreSQL connection failed:", e)

# Upload to PostgreSQL
df.to_sql(name='supermart', con=engine_psql, if_exists='replace', index=False)
print("Data uploaded to PostgreSQL")
