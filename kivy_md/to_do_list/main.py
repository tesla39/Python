from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from database import Database
db = Database()

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
   
    def mark(self, check, list_item):
        '''mark the task as complete or incomplete'''
        if check.active == True:
            list_item.text = '[s]'+list_item.text+'[/s]'
            db.mark_task_as_complete(list_item.pk)
        else:
            list_item.text = str(db.mark_task_as_incomplete(list_item.pk))

    def delete_item(self, list_item):
        '''Delete the task'''
        self.parent.remove_widget(list_item)
        db.delete_task(list_item.pk)
    
    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(LeftCheckbox())
        self.pk = pk

    
class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
    #kwargs is used to pass additional number of arguments than declared 
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)


class MainApp(MDApp):

    def on_start(self):
        """Load the saved tasks and add them to the MDList widget when the application starts"""
        try:
            completed_tasks, uncomplete_tasks = db.get_tasks()

            if uncomplete_tasks != []:
                for task in uncomplete_tasks:
                    add_task = ListItemWithCheckbox(pk=task[0],text=task[1], secondary_text=task[2])
                    self.root.ids.container.add_widget(add_task)

            if completed_tasks != []:
                for task in completed_tasks:
                    add_task = ListItemWithCheckbox(pk=task[0],text='[s]'+task[1]+'[/s]', secondary_text=task[2])
                    add_task.ids.check.active = True
                    self.root.ids.container.add_widget(add_task)
        except Exception as e:
            print(e)
            pass
    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        self.task_list_dialog = None

    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
            )
        self.task_list_dialog.open()

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def add_task(self, task, task_date):
        created_task = db.create_task(task.text, task_date)# Here

        # return the created task details and create a list item
        self.root.ids['container'].add_widget(ListItemWithCheckbox(pk=created_task[0], text='[b]'+created_task[1]+'[/b]', secondary_text=created_task[2]))# Here
        task.text = ''

   


if __name__ == '__main__':
    app = MainApp()
    app.run()