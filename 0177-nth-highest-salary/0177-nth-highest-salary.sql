CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N=N-1;
  RETURN (
    SELECT DISTINCT Salary 
    FROM Employee
    ORDER BY Salary DESC 
    LIMIT 1 OFFSET N
      # Write your MySQL query statement below.

  );
END