from kivy.app import App
from kivy.uix.label import Label
class FirstProject(App):
    def build(self):
        label_obj= Label(text='Hello, World!')
        return label_obj
    
if __name__ == '__main__':
    FirstProject().run()


