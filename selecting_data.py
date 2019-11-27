import sqlite3 as lit


db = lit.connect('employee.db')


with db:
    cur = db.cursor()
    selecquery = "SELECT * FROM users"
    cur.execute(selecquery)

    rows = cur.fetchall()

    for data in rows:
        print(data)
