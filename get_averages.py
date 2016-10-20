import sqlite3

# create db object 
db = sqlite3.connect("stud_info.db")
cur = db.cursor()


def compavg(num):
	tot = 0.0
	n = 0.0
	query = "SELECT grade FROM courses, students WHERE %s == courses.id"%(num)
	sel = (cur.execute(query)).fetchall()
	for item in sel:
		tot += item[0]
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

print compavg(1)
print compavg(2)
print compavg(3)
prinfo()
