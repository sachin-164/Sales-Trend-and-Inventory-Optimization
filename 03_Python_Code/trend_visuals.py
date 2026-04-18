import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

input_file = "04_Clean_Data/final_model_data.csv"
output_folder = "07_Statistical_Visuals"

if not os.path.exists(input_file):
    print(f"❌ Error: {input_file} not found. Please run your Week 6 script first!")
else:
    df = pd.read_csv(input_file)
    os.makedirs(output_folder, exist_ok=True)

    # DAY 23: DEMAND INTENSITY HEATMAP
    # We pivot the data to see Product vs. Fiscal Quarter volume
    pivot_table = df.pivot_table(
        index='Product_Name', 
        columns='Fiscal_Quarter', 
        values='Quantity_Sold_KG', 
        aggfunc='sum'
    ).fillna(0) # Replace missing values with 0 for a cleaner heatmap

    plt.figure(figsize=(14, 10))
    sns.heatmap(pivot_table, annot=False, cmap="YlGnBu", cbar_kws={'label': 'Volume (KG)'})
    plt.title("Heatmap: Export Demand Intensity by Product and Quarter", fontsize=16)
    plt.xlabel("Fiscal Quarter", fontsize=12)
    plt.ylabel("Product Name", fontsize=12)
    
    heatmap_path = os.path.join(output_folder, "01_demand_heatmap.png")
    plt.savefig(heatmap_path, bbox_inches='tight')
    plt.close() # Close to free up memory
    print(f"Heatmap saved: {heatmap_path}")

    # DAY 25: PROFIT CORRELATION SCATTER PLOT 
    # Visualizing how storage duration affects profit margins
    plt.figure(figsize=(12, 7))
    sns.scatterplot(
        data=df, 
        x='Storage_Duration_Days', 
        y='Total_Order_Profit', 
        hue='Spoilage_Risk_Level', 
        palette={'Low': 'green', 'High': 'orange', 'Critical': 'red'},
        alpha=0.6
    )
    plt.title("Correlation: Storage Duration vs. Profitability", fontsize=16)
    plt.xlabel("Days in Warehouse", fontsize=12)
    plt.ylabel("Net Profit per Order", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)

    scatter_path = os.path.join(output_folder, "02_profit_correlation_plot.png")
    plt.savefig(scatter_path, bbox_inches='tight')
    plt.close()
    print(f"Scatter Plot saved: {scatter_path}")

