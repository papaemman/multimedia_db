# Load modules
import psycopg2
import psycopg2.extras

import pandas as pd

# SQL Queries

# - Check database
# - Count files per actor
# - Count faces per images



# Connect to DB
con = psycopg2.connect(
    host = "localhost",
    database = "images",
    user = "postgres",
    password = "pass",
    port = 5432
)

# type(con)
# <class 'psycopg2.extensions.connection'>


# Cursor
cur = con.cursor()

cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

cur.execute("INSERT INTO student (name) VALUES(%s)", ("Antony",))
cur.execute("INSERT INTO student (name) VALUES(%s)", ("Bob",))
cur.execute("INSERT INTO student (name) VALUES(%s)", ("Christina",))

cur.execute("SELECT * FROM student")

print(cur.fetchall())

cur.execute("SELECT * FROM student WHERE id = %s", (1,))
print(cur.fetchall())


# This will close the cursor automatically.
with con.cursor() as cur:
    cur.execute("SELECT * FROM student WHERE id = %s;", (1,))
    print(cur.fetchone())


cur.execute("INSERT INTO employees\
             VALUES (4, 'Anestis', 99, 'anestis@fa.com')")

# Rollback after invalid transaction
cur.execute("ROLLBACK")

# Execute a query
cur.execute("SELECT * FROM employees")

rows =  cur.fetchall()

for r in rows:
    print(r)
 

df = pd.DataFrame(rows)
df.head()

# Commit the transaction
con.commit()

# Close the cursor
cur.close()

# Close the connection
con.close()



if __name__ == "__main__":
    print("Main")