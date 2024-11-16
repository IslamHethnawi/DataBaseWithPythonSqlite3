# read data from table 
import sqlite3
db = sqlite3.connect('movies.db')
cur = db.cursor()
#cur.execute("SELECT title,genre FROM movie")
data = cur.execute("SELECT * FROM movie")
#for row in data:
#  print(row)
for row in data:
    print(row[0])

data = cur.execute("SELECT rowid, * FROM movie")
for row in data:
    print(row[0])

db.commit()
db.close()