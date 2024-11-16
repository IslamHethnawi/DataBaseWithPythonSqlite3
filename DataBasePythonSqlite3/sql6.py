import sqlite3
db = sqlite3.connect('movies.db')
cur = db.cursor()
data = cur.execute("SELECT * FROM movie")
print(     cur.fetchone()   )
print(     cur.fetchmany(1)   )
print(     cur.fetchall()   )
data = cur.fetchall()
for row in data:
    print(row)
    print(row[0])
db.commit()
db.close()