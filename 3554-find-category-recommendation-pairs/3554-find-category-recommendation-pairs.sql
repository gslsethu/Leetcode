# Write your MySQL query statement below
SELECT
    c1.category AS category1,
    c2.category AS category2,
    COUNT(DISTINCT c1.user_id) AS customer_count
FROM (
    SELECT DISTINCT
        pp.user_id,
        pi.category
    FROM ProductPurchases pp
    JOIN ProductInfo pi
        ON pp.product_id = pi.product_id
) c1
JOIN (
    SELECT DISTINCT
        pp.user_id,
        pi.category
    FROM ProductPurchases pp
    JOIN ProductInfo pi
        ON pp.product_id = pi.product_id
) c2
    ON c1.user_id = c2.user_id
   AND c1.category < c2.category
GROUP BY c1.category, c2.category
HAVING COUNT(DISTINCT c1.user_id) >= 3
ORDER BY customer_count DESC,
         category1 ASC,
         category2 ASC;