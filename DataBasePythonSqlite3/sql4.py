# insert list into table
import sqlite3
con=sqlite3.connect('movies.db')
cursor = con.cursor()
movies = [
    ('the godfather','crime',1970),
    ('oppenheimer','drama',2023),
    ('The whale','drama',2024),
    ('Delete History','comedy',2025),
    ('Apples','fantasy',2020),
    ('Nomadland','drama',2021),

]
cursor.executemany("INSERT INTO movie VALUES(?,?,?)", movies)
con.commit()

con.close()