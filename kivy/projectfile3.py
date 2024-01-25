from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

class CalculatorApp(App):
    def build(self):
        return Builder.load_file('calculator.kv')

    def on_start(self):
        for child in self.root.children[0].children:
            if isinstance(child, Button):
                child.bind(on_press=self.on_button_press)
        self.result = self.root.ids.result

    def on_button_press(self, instance):
        current_text = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            self.calculate_result()
        else:
            self.result.text = current_text + button_text

    def calculate_result(self):
        try:
            result = eval(self.result.text)
            self.result.text = str(result)
        except Exception as e:
            self.result.text = 'Error'

if __name__ == '__projectfile3__':
    CalculatorApp().run()