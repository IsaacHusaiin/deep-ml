-- your query
SELECT min(id) as id , email from person
group by email
order by id ASC