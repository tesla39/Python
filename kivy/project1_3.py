
from kivy.app import App
from kivy.uix.textinput import TextInput


class SecondProject(App):
    def build(self):
        textinput = TextInput(text='Enter something')
        return textinput
if __name__ == '__main__':
    SecondProject().run()



