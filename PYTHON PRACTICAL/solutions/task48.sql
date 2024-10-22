SELECT o.order_num,
    o.amount,
    c.name
FROM orders o
    JOIN customers c ON o.customer_id = c.id
WHERE o.amount BETWEEN 500 AND 2000
ORDER BY o.order_num;