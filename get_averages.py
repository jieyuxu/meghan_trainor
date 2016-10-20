import sqlite3

# create db object 
db = sqlite3.connect("stud_info.db")
cur = db.cursor()

def getGrade(num):
	ret = "The grades of the student with id # " + str(num) + " are: "
	query = "SELECT grade FROM courses WHERE %s == courses.id"%(num)
	sel = cur.execute(query)
	for record in sel:
		ret += str(record).strip(')(,') + ", "
	
	return ret[:-2]

def compavg(num):
	tot = 0.0
	n = 0.0
	query = "SELECT grade FROM courses, students WHERE %s == courses.id"%(num)
	sel = cur.execute(query)
	for record in sel:
		tot += float(str(record).strip(')(,')) 
		n+=1
	return tot/n

def prinfo():
	d = {}
	cur.execute("SELECT name,grade,courses.id FROM courses,students WHERE courses.id = students.id")
	r = cur.fetchall()
	for item in r:
		if item[0] not in d.keys():
			d[item[2]] = [item[0], compavg(item[2])]
	
	for item in d:
		print "Name: " + d[item][0] + ", Id: " + str(item) + ", Avg: " + str(d[item][1])

print getGrade(1)
print getGrade(2)
print getGrade(3)
print compavg(1)
print compavg(2)
print compavg(3)
prinfo()
