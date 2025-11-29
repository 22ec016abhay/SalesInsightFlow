-- Calculate Total Revenue by Region
SELECT region, SUM(sales_amount) as total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;

-- Top 5 Selling Products
SELECT product_name, COUNT(*) as total_sold
FROM sales
GROUP BY product_name
ORDER BY total_sold DESC
LIMIT 5;

-- Monthly Sales Trend
SELECT DATE_FORMAT(order_date, '%Y-%m') as month, SUM(sales_amount) as revenue
FROM sales
GROUP BY month
ORDER BY month;
