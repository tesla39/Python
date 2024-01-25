from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SecondProject(App):
    def build(self):
        box = BoxLayout(orientation='horizontal')
        button = Button(text='Click Me')
        box.add_widget(button)
        return box
if __name__ == '__main__':
    SecondProject().run()

"""from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SecondProject(App):
    def build(self):
        box = BoxLayout(orientation='horizontal')
        button = Button(text='Click Me')
        box.add_widget(button)
        return box

if __name__ == '__main__':
    SecondProject().run()"""

