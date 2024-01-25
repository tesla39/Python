
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class SecondProject(App):
    def build(self):
        popup = Popup(title='pop up window', content=Label(text='pop up message'), size_hint=(None, None), size=(400, 400))
        return popup
if __name__ == '__main__':
    SecondProject().run()






