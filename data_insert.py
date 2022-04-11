import psycopg2
from time import time

#Establishing the connection
conn = psycopg2.connect(
   database="currency", user='postgres', password='7153862', host='127.0.0.1', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO prices(time, rub_usd, rub_eur, rub_gbp) VALUES (%s, 0, 0, 0)''', [time()*1000])

# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()