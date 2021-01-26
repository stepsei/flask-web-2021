# INSERT Command


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:

    # insert data
    cursor.execute("INSERT INTO population VALUES('Atlanta', 'GA', 7400000)")
    cursor.execute("INSERT INTO population VALUES('Philadelphia', 'PA', 835000)")

    # commit the changes
    conn.commit()

except sqlite3.OperationalError:
    print("Oops! Something went wront. Try again...")

# close the database connection
conn.close()

