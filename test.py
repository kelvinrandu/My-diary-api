import psycopg2
import os
from psycopg2 import sql


# basic script of testing connection to database

try:
    # connect to database
    conn = psycopg2.connect(
        "dbname=mydiary user=postgres password=1234 host=localhost")
        


except:
    print("database not connected")

user_name =  'makedkna'
user_email = 'randukelvin@gmail.com'
user_password = '1234'
table_name = 'users'
cur = conn.cursor() 


try:
    
    cur.execute("""SELECT * FROM users WHERE email='{}' """.format(user_email))
    rows = cur.fetchone()
    print(rows)



except:
    print("database not connected")





