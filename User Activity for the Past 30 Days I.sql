# Write your MySQL query statement below
select distinct activity_date as day, COUNT(distinct user_id) as active_users
from Activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date
