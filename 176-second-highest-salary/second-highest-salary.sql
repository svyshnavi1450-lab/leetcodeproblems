select(
 select max(Salary) from Employee where salary < (select max(salary) from Employee))as SecondHighestSalary;