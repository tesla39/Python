# demonstrating the use of kivymd

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
Window.size=(350,550)

class ChatBot(MDApp):
     def change_screen(self,name):
        screen_manager.current=name
     def build(self):
         global screen_manager
         screen_manager=ScreenManager()
         screen_manager.add_widget(Builder.load_file("Main.kv"))
         screen_manager.add_widget(Builder.load_file("chat.kv"))
         return screen_manager










import openai
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem

openai.api_key = ''

kv = '''
BoxLayout:
    orientation: 'vertical'

    ScrollView:
        MDList:
            id: chat_list

    MDBoxLayout:
        size_hint_y: None
        height: "40dp"

        MDTextField:
            id: message_input
            hint_text: "Enter message"

        MDIconButton:
            icon: "send"
            on_release: app.send_message()
'''

class ChatApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def send_message(self):
        message = self.root.ids.message_input.text
        self.root.ids.chat_list.add_widget(
            OneLineListItem(text="You: " + message)
        )
        self.root.ids.message_input.text = ''
        self.get_response(message)

    def get_response(self, message):
        # Call OpenAI API to get a response
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=message,
          temperature=0.5,
          max_tokens=100
        )
        self.root.ids.chat_list.add_widget(
            OneLineListItem(text="Bot: " + response.choices[0].text.strip())
        )

if __name__ == '__main__':
    ChatApp().run()













