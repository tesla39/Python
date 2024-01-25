from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView

class ImageViewerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Top row layout to hold label and text input
        top_layout = GridLayout(cols=2, size_hint=(1, 0.1))
        self.image_label = Label(text='Enter image URL:', size_hint_x=0.3)
        self.image_input = TextInput(multiline=False)
        top_layout.add_widget(self.image_label)
        top_layout.add_widget(self.image_input)

        # Image display area
        self.image = Image(size_hint=(1, 0.8))
        
        # Bottom row layout to hold buttons and file chooser
        bottom_layout = GridLayout(cols=4, size_hint=(1, 0.1))
        self.load_button = Button(text='Load', on_press=self.load_image)
        self.clear_button = Button(text='Clear', on_press=self.clear_image)
        self.file_chooser_button = Button(text='Select Image', on_press=self.select_image)
        self.quit_button = Button(text='Quit', on_press=self.quit_app)
        bottom_layout.add_widget(self.load_button)
        bottom_layout.add_widget(self.clear_button)
        bottom_layout.add_widget(self.file_chooser_button)
        bottom_layout.add_widget(self.quit_button)

        layout.add_widget(top_layout)
        layout.add_widget(self.image)
        layout.add_widget(bottom_layout)
        return layout

    def load_image(self, instance):
        image_url = self.image_input.text
        if image_url:
            self.image.source = image_url
            self.image.reload()

    def clear_image(self, instance):
        self.image.source = ''
        self.image.reload()

    def select_image(self, instance):
        file_chooser = FileChooserListView()
        file_chooser.bind(on_submit=self.load_selected_image)
        popup = popup(title='Select an image', content=file_chooser, size_hint=(0.8, 0.8))
        popup.open()

    def load_selected_image(self, instance, selection):
        if selection:
            self.image.source = selection[0]
            self.image.reload()

    def quit_app(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    ImageViewerApp().run()
