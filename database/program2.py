#without database connection

from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Blue"

        return Builder.load_file('kivy1.kv')

MainApp().run()
