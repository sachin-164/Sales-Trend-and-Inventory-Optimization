SELECT 
Product_Name,
SUM(Quantity_Sold_KG) AS total_sales,
AVG(Cost_Per_KG) AS avg_procurement_cost,
SUM(Revenue) AS total_revenue
FROM master_dataset
GROUP BY Product_Name
ORDER BY total_revenue DESC;