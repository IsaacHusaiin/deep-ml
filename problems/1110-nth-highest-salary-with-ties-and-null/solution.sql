-- your query
SELECT (
    SELECT DISTINCT salary
    FROM employee
    WHERE salary IS NOT NULL
    ORDER BY salary DESC
    LIMIT 1 OFFSET 2
) AS nth_salary;
