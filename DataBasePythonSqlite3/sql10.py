#Delete data
import sqlite3
db = sqlite3.connect('movies.db')
cur= db.cursor()



#cur.execute("DELETE FROM movie WHERE rowid BETWEEN 8 AND 9")

cur.execute("DROP TABLE movie")



cur.execute("SELECT rowid, * FROM movie")
data = cur.fetchall()
for row in data:
    print(row)

db.commit()
db.close()