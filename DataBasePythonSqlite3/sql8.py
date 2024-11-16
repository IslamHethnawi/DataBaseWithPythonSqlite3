import sqlite3
db =sqlite3.connect('movies.db')
cur = db.cursor()
#cur.execute("SELECT rowid, * FROM movie WHERE title = 'oppenheimer' ")
#cur.execute("SELECT rowid, * FROM movie WHERE title != 'oppenheimer' ")
#cur.execute("SELECT rowid, * FROM movie WHERE genre ='drama' AND year > 2023  ")
#cur.execute("SELECT rowid, * FROM movie WHERE genre ='drama' OR year > 2023  ")
#cur.execute("SELECT rowid, * FROM movie WHERE genre =LOWER('drama') OR year > 2023  ")
#cur.execute("SELECT rowid, * FROM movie WHERE genre =UPPER('drama') OR year > 2023  ")
#cur.execute("SELECT * FROM movie WHERE genre LIKE 'd%' ") # d%
#cur.execute("SELECT * FROM movie WHERE genre LIKE '%d%' ") # %d%
#cur.execute("SELECT * FROM movie WHERE genre LIKE '%d' ") #%d
#cur.execute("SELECT * FROM movie WHERE genre LIKE '_d%' ")
#cur.execute("SELECT * FROM movie WHERE year BETWEEN 2020 AND 2021 ")
#cur.execute("SELECT rowid, * FROM movie WHERE rowid BETWEEN 1 AND 5   ")
cur.execute("SELECT rowid, * FROM movie WHERE rowid NOT BETWEEN 1 AND 5   ")
data = cur.fetchall()
for row in data:
    print(row)
db.commit()
db.close()