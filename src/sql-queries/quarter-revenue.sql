

-- Initially I have tried a lot to solve the problem, later I took help from ChatGPT, but I would admit, 
-- I am not able to solve it. I know sql but I do not know much advanced sql queries. 
-- I have populated a table with some dummy data, but I could not solve it. I tried to seek help from Chatgpt but it gave too much  
-- complex queries which I did not understand, hence, I decided to just left it as far as I went with the problem. 



SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(total_amount) AS total_revenue
FROM 
    orders
WHERE 
    order_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY 
    DATE_FORMAT(order_date, '%Y-%m')
ORDER BY 
    month;
