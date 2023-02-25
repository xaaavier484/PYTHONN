
import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db succesfully")
conn.execute("CREATE TABLE students "
             "(ID PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL,")

print("Table created successfully")
