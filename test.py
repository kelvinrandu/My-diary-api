import psycopg2
import os

# start here
try:
    # connect to database
    conn = psycopg2.connect(
        "dbname=mydiary user=randu password=1234 host=localhost")
    print("database connected")


except:
    print("database not connected")



# end here



# def create_user:
#     conn.cursor().execute(
#         """INSERT INTO users (user_name, email,created_at)
#         VALUES ('k1ika', 'ke5n@m.com', '1-9-2011')""")