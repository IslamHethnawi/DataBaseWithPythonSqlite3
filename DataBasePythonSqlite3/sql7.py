import sqlite3
db = sqlite3.connect('movies.db')
cur = db.cursor()
#data = cur.execute("SELECT * FROM movie ORDER BY title") #...
#data = cur.execute("SELECT * FROM movie ORDER BY title DESC") #ASC 
data = cur.execute("SELECT * FROM movie ORDER BY title LIMIT 2")
data = cur.fetchall()
for row in data:
    print(row)

db.commit()
db.close()




