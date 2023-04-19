import matplotlib.pyplot as plt
import numpy as np
import pymysql
import csv
import sys
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  db = "sys"
)
mycursor = mydb.cursor()
#total enrollment
sql = """SELECT SUM(n_enrolled) AS total_program_enrollment, COUNT(title) AS num_courses, AVG(price) AS avg_course_purchase, MIN(price) AS min_course_purchase, MAX(price) AS max_course_purchase
FROM `mytable2`
WHERE subject = 'Data Analysis & Statistics'
ORDER BY price DESC"""

mycursor.execute(sql)
records = mycursor.fetchall()
total_program_enrollment = []
num_courses = []
avg_course_purchase = []
min_course_purchase = []
max_course_purchase = []
for i in records:
    total_program_enrollment = float(i[0])
    num_courses= float(i[1])
    avg_course_purchase= float(i[2])
    min_course_purchase= float(i[3])
    max_course_purchase= float(i[4])
fig, ax = plt.subplots() 
var = ['total_program_enrollmentt', 'num_coursess', 'avg_course_purchasee', 'min_course_purchasee', 'max_course_purchasee']
counts = [total_program_enrollment, num_courses, avg_course_purchase, min_course_purchase, max_course_purchase]
bar_labels = ['red', 'blue', '_red', 'orange', 'purple']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:red','tab:orange']
print('prueba', counts)
ax.bar(var, counts, label=bar_labels, color=bar_colors)
plt.title("total program enrollment")
ax.set_ylabel('price')
ax.set_title('price')
ax.legend(title='price color')
plt.show()

print("Total number of rows in table: ", mycursor.rowcount)

print("\nPrinting each row")
for row in records:
    print("total_program_enrollment = ", row[0], )
    print("num_courses = ", row[1])
    print("avg_course_purchase = ", row[2])
    print("max_course_purchase  = ", row[3], "\n")
    #price bucket edx
sqll = """SELECT price, COUNT(price) AS subject_count,
100 * COUNT(price) / (SELECT COUNT(*) FROM mytable2) AS price_pct
FROM `mytable2`
GROUP BY price
ORDER BY price_pct DESC LIMIT 10"""
mycursor.execute(sqll)
records = mycursor.fetchall()
price = []
price_pct = []
subject_count = []
for i in records:
   price.append(float(i[0]))
print("price = ", price)
fig, ax = plt.subplots()
var = ['pricee', 'price2', 'price3', 'price5', 'price6', 'price7', 'price8', 'price9', 'price10', 'price11']
bar_labels = ['blue', 'asd', 'dsadsa', 'adssad', 'red', 'red', 'red', 'red' ,'red', 'red',]
bar_colors = ['tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red']
ax.bar(var, price, label=bar_labels, color= bar_colors)
ax.set_ylabel('price')
ax.set_title('price EDX')
ax.legend(title='price color')
plt.show()
for i in records:
   price_pct.append(float(i[1]))
   print("price_pct = ", price_pct)
fig, ax = plt.subplots()
var = ['pricepct1', 'pricepct2', 'pricepct3', 'pricepct4', 'pricepct5', 'pricepct6', 'pricepct7', 'pricepct8', 'pricepct9', 'pricepct10']
bar_labels = ['blue', 'asd', 'dsadsa', 'adssad', 'red', 'red', 'red', 'red' ,'red', 'red',]
bar_colors = ['tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red']
ax.bar(var, price_pct, label=bar_labels, color= bar_colors)
ax.set_ylabel('price pct')
ax.set_title('price percentage EDX')
ax.legend(title='price color')
plt.show()
for i in records:
   subject_count.append(float(i[1]))
   print("subject count = ", subject_count)
fig, ax = plt.subplots()
var = ['subjectcount1', 'subjectcount2', 'subjectcount3', 'subjectcount4', 'subjectcount5', 'subjectcount6', 'subjectcount7', 'subjectcount8', 'subjectcount9', 'subjectcount10']
bar_labels = ['blue', 'asd', 'dsadsa', 'adssad', 'red', 'red', 'red', 'red' ,'red', 'red',]
bar_colors = ['tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red']
ax.bar(var, subject_count, label=bar_labels, color= bar_colors)
ax.set_ylabel('subject count')
ax.set_title('subject count EDX')
ax.legend(title='price color')
plt.show()
print("\nPrinting each row")
for row in records:
    print("price = ", row[0], )
    print("subject_count = ", row[1])
    print("price_pct = ", row[2])
#price bucket udemy
sqlll = """SELECT price, COUNT(price) AS subject_count,
100 * COUNT(price) / (SELECT COUNT(*) FROM mytable3) AS price_pct
FROM `mytable3`
GROUP BY price
ORDER BY price_pct DESC LIMIT 10"""
mycursor.execute(sqlll)
records = mycursor.fetchall()
price_pct = []
subject_count = []
price = []
for i in records:
   price.append(float(i[0]))
print("price = ", price)
fig, ax = plt.subplots()
var = ['pricee', 'price2', 'price3', 'price5', 'price6', 'price7', 'price8', 'price9', 'price10', 'price11']
bar_labels = ['blue', 'asd', 'dsadsa', 'adssad', 'red', 'red', 'red', 'red' ,'red', 'red',]
bar_colors = ['tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red']
ax.bar(var, price, label=bar_labels, color= bar_colors)
ax.set_ylabel('price')
ax.set_title('price Udemy')
ax.legend(title='price color')
plt.show()
for i in records:
   price_pct.append(float(i[1]))
   print("price_pct = ", price_pct)
fig, ax = plt.subplots()
var = ['pricepct1', 'pricepct2', 'pricepct3', 'pricepct4', 'pricepct5', 'pricepct6', 'pricepct7', 'pricepct8', 'pricepct9', 'pricepct10']
bar_labels = ['economics', 'politics', 'engineering', 'adssad', 'red', 'red', 'red', 'red' ,'red', 'red',]
bar_colors = ['tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red']
ax.bar(var, price_pct, label=bar_labels, color= bar_colors)
ax.set_ylabel('price pct')
ax.set_title('price percentage Udemy')
ax.legend(title='price color')
plt.show()
for i in records:
   subject_count.append(float(i[1]))
   print("subject count = ", subject_count)
fig, ax = plt.subplots()
var = ['subjectcount1', 'subjectcount2', 'subjectcount3', 'subjectcount4', 'subjectcount5', 'subjectcount6', 'subjectcount7', 'subjectcount8', 'subjectcount9', 'subjectcount10']
bar_labels = ['blue', 'asd', 'dsadsa', 'adssad', 'red', 'red', 'red', 'red' ,'red', 'red',]
bar_colors = ['tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red', 'tab:red']
ax.bar(var, subject_count, label=bar_labels, color= bar_colors)
ax.set_ylabel('subject count')
ax.set_title('subject count Udemy')
ax.legend(title='price color')
plt.show()
print("\nPrinting each row")
for row in records:
    print("price = ", row[0], )
    print("subject_count = ", row[1])
    print("price_pct = ", row[2])

db_opts = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'sys'
}

db = pymysql.connect(**db_opts)
cur = db.cursor()

sql = """SELECT price, COUNT(price) AS subject_count,
100 * COUNT(price) / (SELECT COUNT(*) FROM mytable3) AS price_pct
FROM `mytable3`
GROUP BY price
ORDER BY price_pct DESC LIMIT 10"""
csv_file_path = 'C:/Users/M/Desktop/my_csv_file3.csv'

try:
    cur.execute(sql)
    rows = cur.fetchall()
finally:
    db.close()

# Continue only if there are rows returned.
if rows:
    # New empty list called 'result'. This will be written to a file.
    result = list()

    # The row name is the first entry for each entity in the description tuple.
    column_names = list()
    for i in cur.description:
        column_names.append(i[0])

    result.append(column_names)
    for row in rows:
        result.append(row)

    # Write result to file.
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in result:
            csvwriter.writerow(row)
else:
    sys.exit("No rows found for query: {}".format(sql))