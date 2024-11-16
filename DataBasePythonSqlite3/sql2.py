#create tables in the database
import sqlite3
con=sqlite3.connect('movies.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE movie(title TEXT, genre TEXT ,year INTEGER)")

con.commit()

con.close()