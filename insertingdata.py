import sqlite3 as lit


myusers = (
    (1, "user1", "user@email.de"),
    (2, "user2", "user@email.de"),
    (3, "user3", "user@email.de"),
    (4, "user4", "user@email.de")
)

db = lit.connect("employee.db")

with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?)', myusers)

    print("Data inserted successfully.")
