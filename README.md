# **Honey Rich Pvt Ltd: Sales-Trend-and-Inventory-Optimization**

### **📊 Project Overview**
This project was developed during a **10-week Industrial Training program** to optimize inventory and financial tracking for **Honey Rich Pvt Ltd**, a global exporter of agricultural products. The primary goal was to bridge the gap between **procurement costs** and **export sales revenue** to identify profit leakages.

### **🛠️ Technology Stack**
* **SQL:** Relational database mapping and vendor quality scorecards.
* **Python (Pandas/Seaborn):** Advanced financial calculations, date standardization, and risk modeling.
* **Power BI:** Executive-level interactive dashboarding and **DAX measures**.

### **📂 Folder Structure**
* **`01_Original_Files/`**: Raw CSV datasets (Export Sales & Supply Logs).
* **`02_SQL_Logic/`**: SQL scripts for table joins and vendor ranking.
* **`03_Python_Code/`**: Jupyter Notebooks and `.py` scripts for data engineering.
* **`04_Clean_Data/`**: Final processed dataset.
* **`05_PowerBI_Work/`**: Interactive dashboard file (`.pbix`) and DAX formulas.
* **`07_Statistical_Visuals/`**: Automated plots (**Heatmaps** & **Scatter Plots**).

---

### **🚀 Key Findings & Achievements**
* **Unified Data Model:** Successfully reconciled **14,000 export records** with **10,000 procurement entries** using a relational `Batch_ID` join.
* **Risk Identification:** Developed a spoilage logic that identified **4,620 critical batches** sitting in the warehouse for over **25 days**, directly impacting the net margin.
* **Financial Insight:** Proved that **international export markets** contribute **over 60% of net profit**, leading to a recommendation to prioritize export-grade inventory.
* **Interactive Dashboard:** Built a **"Profit Hunter" dashboard** in Power BI allowing management to filter by `Fiscal_Quarter` and `Spoilage_Risk_Level`.

---

### **📖 How to Run the Project**
1.  **Step 1:** Run `03_Python_Code/margin_and_storage_analysis.ipynb` to generate the master financials.
2.  **Step 2:** Run `03_Python_Code/efficiency_analysis.ipynb` to tag spoilage risks.
3.  **Step 3:** Run `03_Python_Code/trend_visuals.py` to generate the statistical charts.
4.  **Step 4:** Open `05_PowerBI_Work/HoneyRich_Dashboard.pbix` to view the interactive insights.

---

### **👤 Author**
**Sachin H D** *Final Year BCA Student (Data Science & Big Data Analytics)* *Yenepoya Institute, Mangalore*
