import sqlite3

# create a database first
class Database:
    # create blueprint of the object
    # then create object instances

    #TODO
    # broken at the moment
    # update, delete, add, and search all stopped working, maybe they need (self)?

    def __init__(self,db):# this syntax is a constructor

    # __init__ is how python creates an initial call when class is instanced.
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS booktable (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()
        conn.close()

    def insert(self,title, author, year, isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO booktable VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()

    def view(self):
        # TODO: doesn't work with (db)
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * from booktable")
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * from booktable WHERE title=? OR author=? or year=? OR isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def delete(self,id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM booktable WHERE id=?",(id,))
        # rows=cur.fetchall()
        conn.commit()
        conn.close()

    def update(self,id, title, author, year, isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE booktable SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn, id))
        conn.commit()
        conn.close()


print("Backend initialized.")

# =======
# =======
# =======
# =======
# D E B U G  O P S
# insert("The Earth", "John Smith", 1918, 91283423)
# insert("The Waves", "John Tyler", 1933, 12387123)
#
# print(view())
# print(search(author="John Tablet"))
# update(1, "The Moon", "John Denver", 3022, 31923)
# print(view())
# update(1, "The Moon", "John Denver", 3022, 31923)
# print("And then...")
# print(view())
