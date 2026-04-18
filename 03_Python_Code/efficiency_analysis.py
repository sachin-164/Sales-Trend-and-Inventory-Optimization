import pandas as pd
import os

# --- STEP 1: LOAD RECONCILED DATA ---
# This looks for the output from Week 5 script
try:
    df = pd.read_csv("04_Clean_Data/master_financials.csv")
    print("master_financials.csv loaded.")
except FileNotFoundError:
    print("File not found.")

# SPOILAGE & AGING LOGIC
# Categorizing risk based on warehouse duration
df['Spoilage_Risk_Level'] = df['Storage_Duration_Days'].apply(
    lambda x: 'Critical' if x > 25 else ('High' if x > 15 else 'Low')
)

# FISCAL QUARTER SEGMENTATION
# Preparing the time-axis for the final dashboard
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
df['Fiscal_Quarter'] = df['Sale_Date'].dt.to_period('Q').astype(str)

# --- STEP 4: SAVE THE GOLD DATASET ---
os.makedirs("04_Clean_Data", exist_ok=True)
df.to_csv("04_Clean_Data/final_model_data.csv", index=False)

print(f"Critical Spoilage Batches Identified: {len(df[df['Spoilage_Risk_Level'] == 'Critical'])}")
print("Final Dataset saved to 04_Clean_Data/final_model_data.csv")