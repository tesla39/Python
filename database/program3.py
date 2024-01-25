#with database connection

from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):
        def build(self):
             
                self.theme_cls.theme_style="Dark"
                self.theme_cls.primary_palette="Blue"

                conn=sqlite3.connect('database2.db')
                c=conn.cursor()
                c.execute(
                """CREATE TABLE if not exists customers(id integer PRIMARY KEY AUTOINCREMENT,name text)""")
                conn.commit()
                conn.close()
                return Builder.load_file('kivy1.kv')
              
        def submit(self):
            conn=sqlite3.connect('database2.db')
            c=conn.cursor()
            c.execute(
    "INSERT INTO customers (name) VALUES (:name)", 
    {'name': self.root.ids.word_input.text}
)

            #message
            self.root.ids.word_label.text=f'{self.root.ids.word_input.text}Added'
            
            #clear the input box
            self.root.ids.word_input.text=' '

            conn.commit()
            conn.close()
    
        def show(self):
           conn=sqlite3.connect('database2.db')
           c=conn.cursor()
           c.execute("SELECT * FROM customers")
           records = c.fetchall()
           word=' '

           #looping through record array

           for record in records:
                 word=f'{word}\n ID: {record[0]}\t, Name:{record[1]}'
                 self.root.ids.word_label.text= f'{word}'
    
           conn.commit()
           conn.close()  
MainApp().run()