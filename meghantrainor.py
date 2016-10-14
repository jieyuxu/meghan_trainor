import sqlite3
import csv

conn = sqlite3.connect('stud_info.db')
c = conn.cursor()

fObj = open("peeps.csv") 
d = csv.DictReader(fObj) #students dict

gObj = open("courses.csv")
g = csv.DictReader(gObj) #course dict


# Create table
c.execute('CREATE TABLE students (name text, age Integer, id Integer)')
c.execute('CREATE TABLE courses (course text, grade Real, id Integer)')

#insert data in students
for data in d:
	c.execute('''insert into students
                 (name, age, id)values(?,?,?)''', 
                 (data['name'], data['age'], data['id']))


for data in g:
	c.execute('''insert into courses
                 (course, grade, id)values(?,?,?)''', 
                 (data['code'], data['mark'], data['id']))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()