# Write your MySQL query statement below
select s.product_id as product_id, s.year as first_year, s.quantity as quantity, s.price as price
from Sales s
join (
    select product_id, min(year) as first_year
    from sales
    group by product_id
) fs
on s.product_id = fs.product_id
where s.year = fs.first_year
