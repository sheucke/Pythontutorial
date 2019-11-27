import sqlite3 as lit


def main():
    try:
        db = lit.connect('employee.db')
        cur = db.cursor()

        tablequery = "CREATE TABLE users (id INT, name TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Table Created Successfully.")

    except:
        print("Unable to create table")

    finally:
        db.close()


if __name__ == "__main__":
    main()
