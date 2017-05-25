import sqlite3

# create a database first
def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS booktable (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn text)")
    conn.commit()
    conn.close()


connect()
