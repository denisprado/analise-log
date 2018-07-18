#Python 2.7.12

import psycopg2
import datetime

conn = psycopg2.connect(dbname="news")
cursor = conn.cursor()
cursor.execute(
    "SELECT articles.title, count(log.path) as n_views from log, articles where log.path = CONCAT('/article/', articles.slug) group by articles.title order by n_views DESC limit 3")

posts = cursor.fetchall()

print("-------------------------")
print("First question: ")
print("-------------------------")
for record in posts:
    print('"'+str(record[0])+'" -- '+str(record[1])+' views')

cursor.execute(
    "SELECT authors.name, count(log.path) as n_views from log, articles, authors where log.path = CONCAT('/article/', articles.slug) and articles.author = authors.id group by authors.name order by n_views DESC")
print(" ")
print("-------------------------")
print("Second question: ")
print("-------------------------")
posts = cursor.fetchall()
for record in posts:
    print(str(record[0])+' -- '+str(record[1])+' views')

cursor.execute(
    "CREATE VIEW total AS SELECT date(time) as day, count(id) AS views FROM log GROUP BY day")
cursor.execute(
    "CREATE VIEW error AS SELECT date(time) as day, count(id) AS views FROM log  WHERE status = '404 NOT FOUND' GROUP BY day")
cursor.execute('select total.day, ROUND(((CAST(error.views AS DECIMAL) / CAST(total.views AS DECIMAL))*100), 2) as percent FROM error, total where total.day = error.day and (CAST(error.views AS DECIMAL) / CAST(total.views AS DECIMAL))*100 > 1')
print(" ")
print("-------------------------")
print("Third question: ")
print("-------------------------")
posts = cursor.fetchall()
for record in posts:
    print(record[0].strftime('%B, %d %Y')+' -- '+str(record[1])+'%')

conn.close()