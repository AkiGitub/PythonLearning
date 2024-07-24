from collections import namedtuple
import sqlite3 
from pathlib import Path
import json

# movies = json.loads(Path('d:\\temp\\jsFile.json').read_text())

# with sqlite3.connect('D:\\temp\\db.sqlite3') as conn:
#      command = "insert into movies values(?,?,?)"
#      for movie in movies:
#          conn.execute(command,tuple(movie.values()))
#      conn.commit() 

#read data 
with sqlite3.connect('d:\\temp\db.sqlite3') as conn:
    command = "select * from Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)  #(1, 'Zogo', 1983)  (2, 'Aki', 1985)
    #after cursor we do not access the data because it is the last part of the file,
    print(cursor.fetchall()) 

EmployeeRecord = namedtuple('EmployeeRecord', 'id, title, year')

with sqlite3.connect('d:\\temp\db.sqlite3') as conn:
    cursor = conn.cursor()
    cursor.execute("select id, title, year from Movies")

    for emp in map(EmployeeRecord._make,cursor.fetchall()):
        print(emp.id,emp.title)