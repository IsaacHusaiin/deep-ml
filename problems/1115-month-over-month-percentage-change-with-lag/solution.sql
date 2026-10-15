WITH monthly AS (
    SELECT DATE_TRUNC('month', sale_date) AS month,
           SUM(amount) AS total
    FROM sales
    GROUP BY DATE_TRUNC('month', sale_date)
),
with_prev AS (
    SELECT month,
           total,
           LAG(total) OVER (ORDER BY month) AS prev_total
    FROM monthly
)
SELECT month,
       total,
       ROUND((total - prev_total) * 100.0 / NULLIF(prev_total, 0), 2) AS pct_change
FROM with_prev
ORDER BY month ASC;