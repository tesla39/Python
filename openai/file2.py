from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import IconLeftWidget
import openai

openai.api_key = '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'

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

<BotMessage>:
    IconLeftWidget:
        icon: "robot"

<UserMessage>:
    IconLeftWidget:
        icon: "account"
'''

class BotMessage(OneLineAvatarListItem):
    divider = None
    _no_ripple_effect = True

class UserMessage(OneLineAvatarListItem):
    divider = None
    _no_ripple_effect = True

class ChatApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def send_message(self):
        message = self.root.ids.message_input.text
        self.root.ids.chat_list.add_widget(
            UserMessage(text="You: " + message)
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
            BotMessage(text="Bot: " + response.choices[0].text.strip())
        )

if __name__ == '__main__':
    ChatApp().run()