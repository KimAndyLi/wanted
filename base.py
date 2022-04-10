import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="currency", user='postgres', password='7153862', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS currency")

#Creating table as per requirement
sql ='''CREATE TABLE currency(
   price FLOAT NOT NULL
)'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()