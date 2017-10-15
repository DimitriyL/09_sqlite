import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

peeps = csv.DictReader(open("peeps.csv"))
courses = csv.DictReader(open("courses.csv"))

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

for row in peeps:
    command = "INSERT INTO peeps VALUES(" + row['name'] + "," + row['age'] + "," + row['id'] + ")"          #put SQL statement in this string
    c.execute(command)    #run SQL statement

for row in courses:
    command = "INSERT INTO courses VALUES(" + row['code'] + "," + row['mark'] + "," + row['id'] + ")"          #put SQL statement in this string
    c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database


