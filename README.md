# WEBSITE'S LOG
### this is a log analysis of a website

### _How to run it_:
There is a single python file called log.py. It queries the website's database and prints the results.
#### _the queries are:_
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Defined views:

* **errors** view

`create view errors as
  select to_char(time, 'month dd, yyyy') as day, count(*) as total from log
  where status like '%404%' group by day;`

* **requests** view

`create view requests as
 select to_char(time, 'month dd, yyyy') as day, count(*) as total from log group by day`
