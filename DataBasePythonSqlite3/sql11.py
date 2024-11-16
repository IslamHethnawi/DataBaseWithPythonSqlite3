import sqlite3
db = sqlite3.connect('movies.db')
cur= db.cursor()


cur.execute("DROP TABLE users")
#............................

#cur.execute("CREATE TABLE IF NOT EXISTS x(name TEXT)")
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER

)""")
#cur.execute("INSERT INTO users(user_id ,name,age) VALUES(2,'ahmed', 17)")
cur.execute("INSERT INTO users(name,age) VALUES('islam',17)")
cur.execute("SELECT * FROM users")
data =cur.fetchall()
for row in data:
    print(row)


db.commit()
db.close()