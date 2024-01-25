from kivy.lang import Builder
from kivymd.app import MDApp

from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDToolbar

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'My App'
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: 1, 1, 1, 1

    FloatLayout:

        MDFloatingActionButton:
            icon: 'plus'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_press: app.show_dialog()
'''


class MyApp(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(title='Hello!', text='This is a dialog box.')
        self.dialog.open()


if __name__ == '__main__':
    MyApp().run()