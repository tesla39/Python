from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class FirstProject(App):
    def build(self):
        box_obj = BoxLayout(orientation='horizontal')
        label1 = Label(text='Hello, Kivy!'+'how are you')
        label2 = Label(text='This is a second line of text.')
        
        box_obj.add_widget(label1)
        box_obj.add_widget(label2)
        return box_obj
    
if __name__ == '__main__':
    FirstProject().run()

