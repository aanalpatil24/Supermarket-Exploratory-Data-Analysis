# Supermart Project Analysis in Python

import pandas as pd
import numpy as np

# -----------------------------
# Load Data
# -----------------------------
# Example: reading from CSV
# df = pd.read_csv("supermart.csv")

# For demonstration, creating empty DataFrame with same columns
columns = ['invoice_id', 'branch', 'city', 'category', 'quantity', 'unit_price',
           'total', 'date', 'time', 'payment_method', 'rating', 'profit_margin']
df = pd.DataFrame(columns=columns)

# Convert columns to proper data types
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
df['quantity'] = df['quantity'].astype(float)
df['unit_price'] = df['unit_price'].astype(float)
df['total'] = df['total'].astype(float)
df['rating'] = df['rating'].astype(float)
df['profit_margin'] = df['profit_margin'].astype(float)

# -----------------------------
# Basic Exploration
# -----------------------------
print("Total records:", len(df))
print("Total branches:", df['branch'].nunique())
print("Min quantity sold:", df['quantity'].min())
print(df['payment_method'].value_counts())

# -----------------------------
# Q1: Payment methods, number of transactions, quantity sold
# -----------------------------
q1 = df.groupby('payment_method').agg(
    no_payments=('invoice_id','count'),
    no_qty_sold=('quantity','sum')
).reset_index()
print(q1)

# -----------------------------
# Q2: Highest-rated category in each branch
# -----------------------------
q2 = df.groupby(['branch','category']).agg(avg_rating=('rating','mean')).reset_index()
q2['rank'] = q2.groupby('branch')['avg_rating'].rank(ascending=False, method='dense')
q2 = q2[q2['rank']==1].sort_values('branch')
print(q2[['branch','category','avg_rating']])

# -----------------------------
# Q3: Busiest day for each branch
# -----------------------------
df['day_name'] = df['date'].dt.day_name()
q3 = df.groupby(['branch','day_name']).agg(no_transactions=('invoice_id','count')).reset_index()
q3['rank'] = q3.groupby('branch')['no_transactions'].rank(ascending=False, method='dense')
q3 = q3[q3['rank']==1].sort_values('branch')
print(q3[['branch','day_name','no_transactions']])

# -----------------------------
# Q4: Total quantity sold per payment method
# -----------------------------
q4 = df.groupby('payment_method')['quantity'].sum().reset_index(name='no_qty_sold')
print(q4)

# -----------------------------
# Q5: Avg, min, max rating of categories per city
# -----------------------------
q5 = df.groupby(['city','category']).agg(
    min_rating=('rating','min'),
    max_rating=('rating','max'),
    avg_rating=('rating','mean')
).reset_index()
print(q5)

# -----------------------------
# Q6: Total profit per category
# -----------------------------
q6 = df.groupby('category').apply(lambda x: (x['unit_price']*x['quantity']*x['profit_margin']).sum()).reset_index(name='total_profit')
q6 = q6.sort_values('total_profit', ascending=False)
print(q6)

# -----------------------------
# Q7: Most common payment method per branch
# -----------------------------
q7 = df.groupby(['branch','payment_method']).size().reset_index(name='total_trans')
q7['rank'] = q7.groupby('branch')['total_trans'].rank(ascending=False, method='dense')
q7 = q7[q7['rank']==1].sort_values('branch')
q7 = q7[['branch','payment_method']].rename(columns={'payment_method':'preferred_payment_method'})
print(q7)

# -----------------------------
# Q8: Categorize sales into Morning, Afternoon, Evening shifts
# -----------------------------
def assign_shift(time):
    if time.hour < 12:
        return 'Morning'
    elif 12 <= time.hour <= 17:
        return 'Afternoon'
    else:
        return 'Evening'

df['shift'] = df['time'].apply(assign_shift)
q8 = df.groupby(['branch','shift']).size().reset_index(name='num_invoices')
q8 = q8.sort_values(['branch','num_invoices'], ascending=[True, False])
print(q8)

# -----------------------------
# Q9: Top 5 branches with highest revenue decrease (2022 vs 2023)
# -----------------------------
revenue_2022 = df[df['date'].dt.year==2022].groupby('branch')['total'].sum().reset_index(name='revenue_2022')
revenue_2023 = df[df['date'].dt.year==2023].groupby('branch')['total'].sum().reset_index(name='revenue_2023')
revenue_compare = pd.merge(revenue_2022, revenue_2023, on='branch')
revenue_compare['revenue_decrease_ratio'] = ((revenue_compare['revenue_2022'] - revenue_compare['revenue_2023']) / revenue_compare['revenue_2022'] * 100).round(2)
q9 = revenue_compare[revenue_compare['revenue_decrease_ratio']>0].sort_values('revenue_decrease_ratio', ascending=False).head(5)
print(q9)

# -----------------------------
# Q10: Branch–category with >2 low-rated feedbacks (rating<3.0)
# -----------------------------
q10 = df[df['rating']<3.0].groupby(['branch','category']).size().reset_index(name='low_rating_count')
q10 = q10[q10['low_rating_count']>2].sort_values(['low_rating_count','branch','category'], ascending=[False,True,True])
print(q10)

# -----------------------------
# End of Supermart Project
# -----------------------------
