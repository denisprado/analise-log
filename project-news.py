#!/usr/bin/env python
# encoding: utf-8

import psycopg2
import datetime

conn = psycopg2.connect(dbname="news")
cursor = conn.cursor()

query1 = '''
SELECT articles.title, count(log.path) AS n_views
FROM log, articles
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY n_views DESC
LIMIT 3
'''
# Primeira Questão
cursor.execute(query1)
posts1 = cursor.fetchall()
print("-------------------------")
print("First question: ")
print("-------------------------")
for record in posts1:
    print('"'+str(record[0])+'" -- '+str(record[1])+' views')

query2 = '''
SELECT authors.name, count(log.path) AS n_views
FROM log, articles, authors
WHERE log.path = CONCAT('/article/', articles.slug)
AND articles.author = authors.id
GROUP BY authors.name
ORDER BY n_views DESC
'''
# Segunda questão
cursor.execute(query2)
print(" ")
print("-------------------------")
print("Second question: ")
print("-------------------------")
posts2 = cursor.fetchall()
for record in posts2:
    print(str(record[0])+' -- '+str(record[1])+' views')

query3 = '''
SELECT total.day,
ROUND(((CAST(error.views AS DECIMAL)
/ CAST(total.views AS DECIMAL))*100), 2)
AS percent
FROM error, total
WHERE total.day = error.day
AND (CAST(error.views AS DECIMAL) / CAST(total.views AS DECIMAL))*100 > 1'''
# Terceira questão
cursor.execute(query3)
print(" ")
print("-------------------------")
print("Third question: ")
print("-------------------------")
posts3 = cursor.fetchall()
for record in posts3:
    print(record[0].strftime('%B, %d %Y')+' -- '+str(record[1])+'%')


conn.close()
