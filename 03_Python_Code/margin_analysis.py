import pandas as pd
import os

# Use the exact names you have in your 01_Original_Files folder
sales = pd.read_csv("01_Original_Files/honeyrich_export_sales.csv")
supply = pd.read_csv("01_Original_Files/honeyrich_supply_logs.csv")

# --- DAY 16: The Join ---
df = pd.merge(sales, supply, on='Batch_ID', how='inner')

# --- DAY 17: Margin Calculations ---
# Profit = Revenue - Cost
df['Profit_Per_KG'] = df['Selling_Price_Per_KG'] - df['Cost_Per_KG']
# Margin % = (Profit / Selling Price) * 100
df['Margin_Pct'] = (df['Profit_Per_KG'] / df['Selling_Price_Per_KG']) * 100
# Total Profit for the entire batch sold
df['Total_Order_Profit'] = df['Profit_Per_KG'] * df['Quantity_Sold_KG']

# --- DAY 18: Storage Duration Analysis ---
# FIX: Use 'mixed' format and 'dayfirst' to handle the company's inconsistent date styles
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'], format='mixed', dayfirst=True)
df['Procurement_Date'] = pd.to_datetime(df['Procurement_Date'], format='mixed', dayfirst=True)

# Calculate days in warehouse
df['Storage_Duration_Days'] = (df['Sale_Date'] - df['Procurement_Date']).dt.days

# Save the master financials
os.makedirs("04_Clean_Data", exist_ok=True)
df.to_csv("04_Clean_Data/master_financials.csv", index=False)