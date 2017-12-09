#!/usr/bin/env python3

import psycopg2

con = psycopg2.connect('dbname=project user=postgres password=icandoit')
cursor = con.cursor()
query_1 = ("select articles.title, count(*) as views from articles"
           + " join log on articles.slug like ('%' || articles.slug || '%')  "
           + " group by articles.title order by views desc limit 3;")

query_2 = ("select authors.name, count(*) as views from"
           + " (authors left join articles on authors.id=articles.author)"
           + "left join log on articles.slug like ('%' || articles.slug)"
           + "group by name order by views desc;")

query_3 = ("select errors.day,"
           + " round((errors.total)/(requests.total)::decimal, 2)" +
           " *100.0 as percentage from errors, "
           + " requests where errors.day=requests.day and ("
           + " round((errors.total)/(requests.total)::decimal, 2)"
           + " * 100.0) > 1.0 ;")

cursor.execute(query_1)
con.commit()
result = cursor.fetchall()
cursor.execute(query_2)
con.commit()
result1 = cursor.fetchall()
cursor.execute(query_3)
con.commit()
result2 = cursor.fetchall()
print("the most popular 3 articles of all time: ")
print
for x in result:
    print(x[0], "__", x[1], "views")

print()

print("the most popular article authors: ")
print
for i in result1:
    print(i[0], "__", i[1], " views")


print("days on which errors in requests are more than 1%: ")
for k in result2:
    print(k[0], "__", k[1], "%", " errors")


print
cursor.close()
