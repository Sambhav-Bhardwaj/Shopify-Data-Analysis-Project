SELECT COUNT(*) FROM shopify_sales;

SELECT * FROM shopify_sales LIMIT 5;

SELECT SUM(Net_Sales) AS Total_Sales FROM shopify_sales;

SELECT SUM(`Total Price Usd`) AS Total_Sales 
FROM `shopify_sales`;

SELECT COUNT(`Order Number`) AS Total_Orders 
FROM `shopify_sales`;

SELECT COUNT(DISTINCT `Customer Id`) AS Total_Customers 
FROM `shopify_sales`;

SELECT AVG(`Total Price Usd`) AS Avg_Order_Value 
FROM `shopify_sales`;

-- Top Product Types
SELECT `Product Type`, 
       SUM(`Total Price Usd`) AS Revenue
FROM `shopify_sales`
GROUP BY `Product Type`
ORDER BY Revenue DESC;

-- Low Performing Products
SELECT `Product Type`, 
       SUM(`Total Price Usd`) AS Revenue
FROM `shopify_sales`
GROUP BY `Product Type`
ORDER BY Revenue ASC;

-- Payment Method Analysis
SELECT Gateway, 
       COUNT(*) AS Total_Orders
FROM `shopify_sales`
GROUP BY Gateway;

-- Top Cities by Sales
SELECT CITY, 
       SUM(`Total Price Usd`) AS Revenue
FROM `shopify_sales`
GROUP BY CITY
ORDER BY Revenue DESC
LIMIT 10;

-- Repeat Customers 
SELECT `Customer Id`, COUNT(*) AS Orders
FROM `shopify_sales`
GROUP BY `Customer Id`
HAVING COUNT(*) > 1;

-- Date-wise Sales Trend 
SELECT `Invoice Date`, 
       SUM(`Total Price Usd`) AS Daily_Sales
FROM `shopify_sales`
GROUP BY `Invoice Date`
ORDER BY `Invoice Date`;

-- Top 5 Customers 
SELECT `Customer Id`, 
       SUM(`Total Price Usd`) AS Total_Spent
FROM `shopify_sales`
GROUP BY `Customer Id`
ORDER BY Total_Spent DESC
LIMIT 5;


-- Country-wise Sales
SELECT `Billing Address Country`, 
       SUM(`Total Price Usd`) AS Revenue
FROM `shopify_sales`
GROUP BY `Billing Address Country`
ORDER BY Revenue DESC;


-- Average Quantity per Order
SELECT AVG(Quantity) AS Avg_Quantity 
FROM `shopify_sales`;


-- Highest Order Value 
SELECT MAX(`Total Price Usd`) AS Highest_Order 
FROM `shopify_sales`; 


-- Lowest Order Value
SELECT MIN(`Total Price Usd`) AS Lowest_Order 
FROM `shopify_sales`;