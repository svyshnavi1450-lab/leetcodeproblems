# Write your MySQL query statement below
select user_id as buyer_id,join_date,count(buyer_id) as orders_in_2019
from users u left join orders o
on user_id = buyer_id and year(order_date)="2019"
group by user_id
