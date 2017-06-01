import sqlite3

# create a database first
def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS booktable (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    # reuse all connection standards ==============
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO booktable VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    # reuse all connection standards ==============
    cur=conn.cursor()
    cur.execute("SELECT * from booktable")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    # reuse all connection standards ==============
    cur=conn.cursor()
    cur.execute("SELECT * from booktable WHERE title=? OR author=? or year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect("books.db")
    # reuse all connection standards ==============
    cur=conn.cursor()
    cur.execute("DELETE FROM booktable WHERE id=?",(id,))
    # rows=cur.fetchall() 
    #     isn't used here
    conn.commit()
    conn.close()
    

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    # reuse all connection standards ==============
    cur=conn.cursor()
    cur.execute("UPDATE booktable SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn, id))
    conn.commit()
    conn.close()

def intro(text):
    # other params include expression, sides!
    if text==1:
        print("initializing...")

intro(1)

connect()

# =======
# =======
# =======
# =======

insert("The Earth", "John Smith", 1918, 91283423)
insert("The Waves", "John Tyler", 1933, 12387123)

print(view())
# TESTS
#print(search(author="John Tablet"))
#update(1,"Every Little Thing","Mr So And So", 2017, 543431)
#print(view())
#print("And then...")
print(view())
