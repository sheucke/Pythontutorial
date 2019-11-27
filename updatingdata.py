import sqlite3 as lit


db = lit.connect('employee.db')

with db:
    newname = "updated name"
    user_id = 1
    cur = db.cursor()
    cur.execute('UPDATE users SET name = ? WHERE id = ?', (newname, user_id))
    db.commit()
    print("Data updated succesfully")
