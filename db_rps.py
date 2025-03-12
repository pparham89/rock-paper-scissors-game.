import sqlite3
con = sqlite3.connect('c:/Users/89parham/Documents/database1.db')
cur = con.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS result (id integer PRIMARY KEY,fname text, win real,lose real)')
    con.commit()
def insert_record(fname):
    cur.execute('insert into student values (NULL,?)' ,(fname))
    con.commit()
create_table()
def select_record():
    cur.execute('SELECT * FROM result')
    return cur.fetchall()

def delete_recored(id):
    cur.execute('DELETE FROM student WHERE id= ?', (id,))