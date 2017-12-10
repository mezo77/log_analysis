#!/usr/bin/env python3

import psycopg2

con = psycopg2.connect('dbname=news')
cursor = con.cursor()
query_1 = """
 select articles.title,
        count(*) as views
from articles
     join log on log.path like ('%' || articles.slug)
group by articles.title
order by views desc limit 3;
"""

query_2 = """
      select authors.name, count(*) as views from
         (authors left join articles on authors.id=articles.author)
         left join log on log.path = '/article/' || articles.slug
         group by name
         order by views desc;
"""

query_3 = """
    select errors.day,
           (100)*(round((errors.total)/(requests.total)::numeric, 2))
                as percentage
                 from errors, requests
     where errors.day=requests.day
     and (100)*(round((errors.total)/(requests.total)::numeric, 2)) > 1.0 ;
"""


cursor.execute(query_1)
result1 = cursor.fetchall()

cursor.execute(query_2)
result2 = cursor.fetchall()

cursor.execute(query_3)
result3 = cursor.fetchall()

print("\nthe most popular 3 articles of all time: \n")
for title, views in result1:
    print("{} __ {} views".format(title, views))

print("\nthe most popular article authors: \n")
for title, views in result2:
    print("{} __ {} views".format(title, views))


print("\ndays on which errors in requests are more than 1%: \n")
for title, errors in result3:
    print("{} __ {} {} errors ".format(title, errors, "%"))


cursor.close()
