import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="currency", user='postgres', password='7153862', host='127.0.0.1', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * from currency''')

#Fetching 1st row from the table
result = cursor.fetchone();
# print(result)

#Fetching all rows from the table
result = cursor.fetchall();
# print(result[-1][0])
# value = float(result[-1][0])
# print(type(value))
print(result)
print(type(result))
# print(type(result))
# for i in result:
#     value = float(i[0])
#     print(value)
#     print(type(value))

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()