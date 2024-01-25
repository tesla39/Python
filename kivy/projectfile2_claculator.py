from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operations = ['+', '-', '*', '/']
        self.last_button = None
        self.result = TextInput(font_size=32, multiline=False, readonly=True, halign='right')
        layout = GridLayout(cols=4)

        # Create buttons for digits (0-9) and operators
        buttons = [Button(text=str(i), on_press=self.on_button_press) for i in range(10)]
        buttons += [Button(text=op, on_press=self.on_button_press) for op in self.operations]
        buttons.append(Button(text='C', on_press=self.clear_result))
        buttons.append(Button(text='=', on_press=self.calculate_result))

        # Add the buttons to the layout
        for button in buttons:
            layout.add_widget(button)

        layout.add_widget(self.result)
        return layout

    def on_button_press(self, instance):
        current_text = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        else:
            self.result.text = current_text + button_text

    def clear_result(self, instance):
        self.result.text = ''

    def calculate_result(self, instance):
        try:
            result = eval(self.result.text)
            self.result.text = str(result)
        except Exception as e:
            self.result.text = 'Error'

if __name__ == '__main__':
    CalculatorApp().run()
