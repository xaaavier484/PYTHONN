
import sqlite3
conn=sqlite3.connect('emobilis.db')
print("oppened db succesfully")

conn.execute("INSERT INFO students(ID,NAME,AGE,SCHOOL) VALUES (1,'Xavier',17,'eMobilis')")
conn.execute("INSERT INFO students(ID,NAME,AGE,SCHOOL) VALUES (1,'Aisha',17,'eMobilis')")
conn.execute("INSERT INFO students(ID,NAME,AGE,SCHOOL) VALUES (1,'Lorna',20,'eMobilis')")
conn.execute("INSERT INFO students(ID,NAME,AGE,SCHOOL) VALUES (1,'Ginny',17,'eMobilis')")
conn.commit()
print("records added successfully")
conn.()
