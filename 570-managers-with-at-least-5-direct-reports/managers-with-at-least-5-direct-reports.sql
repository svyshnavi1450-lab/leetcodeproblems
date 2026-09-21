# Write your MySQL query statement below
select e.name as name
from employee as e inner join employee as m
where e.id=m.managerId
group by e.id
having count(e.id)>=5