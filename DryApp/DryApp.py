from re import search
from kivy.uix.accordion import StringProperty

from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.filechooser import FileChooserLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.filechooser import FileChooser
from kivy.uix.filechooser import ScreenManager,Screen
from kivymd.uix.filemanager import MDFileManager
import os
import select
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import StringProperty
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDButton ,MDButtonText
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.screen import MDScreen


class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class Screen4(Screen):
    pass

class Screen5(Screen):
    pass

class MyScreen(MDScreen):  
    name = StringProperty()
    path_to_file = StringProperty()
    album = StringProperty()

class DryApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path, icon_selection_button="home",search= 'all', 
        )

    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Lightblue"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        return Builder.load_file("DryApp.kv")
    
    def change_theme(self):
        self.theme_cls.primary_palette = (
            "Lightblue" if self.theme_cls.primary_palette == "Lightblue" else "Lightblue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        
    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))
        self.manager_open = True

    def file_manager_open_video(self):
        self.open_filtered_file_manager(['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webmv', '.mpeg', '.avchd', '.3gp'])

    def file_manager_open_audio(self):
        self.open_filtered_file_manager(['.mp3', '.wav', '.aac', '.flac', '.ogg', '.aiff', '.wma', '.m4a', '.ape', '.tta'])

    def file_manager_open_image(self):
        self.open_filtered_file_manager(['.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.raw', '.svg', '.ico', '.heic'])

    def file_manager_open_document(self):
        self.open_filtered_file_manager(['.pdf', '.docx', '.odt', '.rtf', '.txt', '.xlsx', '.odp', '.pptx', '.html', '.json'])

    def file_manager_open_autre(self):
        self.open_filtered_file_manager(['.zip', '.rar','.exe', '.app', '.apk', '.iso', '.bat', '.sh', '.sql', '.db', '.xml', '.csv', '.py','.kv'])

    def open_filtered_file_manager(self, extensions):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path,icon_selection_button="home",search= 'all',   
        )
        self.file_manager.ext = extensions
        self.file_manager.show(os.path.expanduser("~"))
        self.manager_open = True

    def select_path(self, path: str):
        self.exit_manager()
        MDSnackbar(
            MDSnackbarText(
                text=path,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
        ).open()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keycode[1] == 'escape':
            if self.manager_open:
                self.file_manager.back()
        return True
    
    def show_filechooser(self):
        self.root.ids.filechooser.show()
        
    def selected_file(self, selection):
        if selection:
            self.root.ids.pdf_label.text = f"PDF : {selection[0]}"  
        
         
if __name__=="__main__":   
    DryApp().run()