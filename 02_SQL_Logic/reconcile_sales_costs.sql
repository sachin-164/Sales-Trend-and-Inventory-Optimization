SELECT 
    S.Order_ID,
    S.Batch_ID,        -- Unique Reference Key
    P.Product_Name,
    P.Cost_Per_KG,      
    S.Selling_Price_Per_KG, 
    S.Quantity_Sold_KG,
    S.Sale_Date,
    P.Procurement_Date
FROM Export_Sales_Log S
INNER JOIN Warehouse_Supply_Log P 
    ON S.Batch_ID = P.Batch_ID;