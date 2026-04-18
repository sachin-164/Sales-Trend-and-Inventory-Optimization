/* Vendor Reliability Scorecard
   Ranking suppliers by Quality and Profit Contribution
*/

SELECT 
    Vendor_Name,
    AVG(Defect_Rate_Pct) AS Avg_Defect_Rate,
    SUM(Total_Order_Profit) AS Total_Profit_Generated,
    COUNT(Batch_ID) AS Total_Batches_Supplied
FROM Final_Model_Data
GROUP BY Vendor_Name
ORDER BY Avg_Defect_Rate ASC; -- Best quality vendors at the top