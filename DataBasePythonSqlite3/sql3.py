# insert row into table
import sqlite3
con=sqlite3.connect('movies.db')
cursor = con.cursor()
#cursor.execute("INSERT INTO  movie(title,genre) VALUES('oppenheimer','drama)")
cursor.execute("INSERT INTO movie VALUES('oppenheimer','drama', 2024)")
con.commit()

con.close()