import sqlite3
conn=sqlite3.connect("database1.db")
conn.execute(''' 
             Create table student(
             id INT AUTO_INCREMENT PRIMARY KEY,
             name VARCHAR(30))
             ''')
conn.close()