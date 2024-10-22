BEGIN;
INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES (3006, 'Stefan Huk', 'Kyiv', 500, 5007);
SELECT *
FROM customers
WHERE city IN ('London', 'Kyiv')
ORDER BY id;
COMMIT;