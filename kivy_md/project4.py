from kivymd.app import MDApp
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.boxlayout import BoxLayout

class MyListItem(TwoLineAvatarIconListItem, ILeftBodyTouch):
    # Implement the required methods from ILeftBodyTouch
    def on_touch_down(self, touch):
        if self.ids['avatar'].collide_point(*touch.pos):
            print("Avatar icon touched!")

class MyApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        
        # Create an instance of MyListItem
        item = MyListItem(text="Primary Text", secondary_text="Secondary Text")
        layout.add_widget(item)
        
        return layout

if __name__ == '__main__':
    MyApp().run()
