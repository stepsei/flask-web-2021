# SEARCH statement

# import the sqlite library
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")
    
    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row (using index notation)
    for r in rows:
        print(r[0], r[1])
