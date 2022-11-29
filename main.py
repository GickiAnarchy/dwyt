
""" Down With YouTube :: Main.py || email: fatheranarchy@programmer.net """

import os

''' YouTube '''
from pytube import YouTube, Search
import yt_dlp

''' Kivy '''
#   App
from kivy.app import App
#   Base Window
from kivy.core.window import Window, WindowBase, EventLoop
#   Clock
from kivy.clock import Clock
#   Canvas
from kivy.graphics import Canvas, Color, Rectangle, Ellipse
#   Layouts
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
#   Screens and Pages
from kivy.uix.screenmanager import Screen, ScreenManager, RiseInTransition, ShaderTransition
#   Base Widget
from kivy.uix.widget import Widget
#   User Interactive Widgets
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
#   Properties
from kivy.properties import ObjectProperty, StringProperty, ListProperty, BooleanProperty, NumericProperty
#   Misc Kivy
from kivy.logger import Logger
from kivy.config import Config
#   Kivy Utils
from kivy.utils import platform

Config.set("graphics", "resizable", True)
EventLoop.ensure_window()
window = EventLoop.window

# Download dir??
DOWNLOADS = "Downloads/"


class Front_Screen(Screen):

    def do_about(self):
        self.popup = Popup(title="ABOUT",
                           content=Label(text="Made by:\nGickiAnarchy\nEmail:fatheranarchy@programmer.net"),
                           size_hint=(0.6, 0.6))
        self.popup.open()


class Search_Screen(Screen):
    pass


class Search_Item(BoxLayout):
    title = StringProperty()
    author = StringProperty()
    url = StringProperty()

    def download(self):
        with yt_dlp.YoutubeDL() as ytdl:
            ytdl.download(self.url)
            return


class Search_Results(RecycleView):
    data = ListProperty([])

    def update_data(self, inp):
        Logger.info(f"update_data called. {inp}")
        if inp in (None,""):
            return False
        try:
            sch = Search(inp)
        except:
            Logger.error("Error in search input")
            return False
        new_data = sch.results
        sch.get_next_results()
        self.data = [{"title": x.title, "author": x.author, "url": x.watch_url} for x in new_data]
        self.refresh_from_data()


class Download_Screen(Screen):
    dl_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Download_Screen, self).__init__(**kwargs)
        self.dl_input = self.ids['dl_input']

    def download(self, format=""):
        url = self.dl_input.text
        try:
            y = YouTube(url)
            self.pop = Popup(title="Download", content=Label(text=f"{y.title}\nPosted By:\n{y.author}"))
            self.pop.open()
        except:
            Logger.error("Not a valid YouTube link")
        if format == "V":
            self.get_video(url)
            return True
        if format == "A":
            self.get_audio(url)
            return True
        if format in (None, ""):
            Logger.warning("Input shouldn't be empty")
            return False

    def get_audio(self, link):
        try:
            yt = YouTube(link)
        except:
            Logger.exception("YouTube link is invalid")
            return False
        audio = yt.streams.get_audio_only()
        destination = f"{DOWNLOADS}/Audio"
        try:
            out_file = audio.download(output_path=destination)
        except:
            err_link = f"::ERROR::\n{link}"
            Logger.error(err_link)
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    def get_video(self, link):
        try:
            yt = YouTube(link)
        except:
            Logger.exception("YouTube link is invalid")
            return False
        video = yt.streams.first()
        destination = f"{DOWNLOADS}/Video"
        try:
            out_file = video.download(output_path=destination)
        except:
            Logger.error(f"::ERROR::\n{link}")
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)


class Page_Master(ScreenManager):
    def __init__(self, **kwargs):
        super(Page_Master, self).__init__(**kwargs)
        self.transition = ShaderTransition()
        self.add_widget(Front_Screen(name='front_screen'))
        self.add_widget(Search_Screen(name='search_screen'))
        self.add_widget(Download_Screen(name='download_screen'))

    def to_home(self):
        self.current = 'front_screen'


class Fa_Window(RelativeLayout):
    pass


class FaApp(App):
    win = ObjectProperty(None)

    def build(self):
        Logger.info("\n\tstarting FaApp")
        return Fa_Window()

    def on_start(self):
        super(FaApp, self).on_start()
        self.win = window
        self.size = self.win.size
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
            def callback(permission, results):
                if all([res for res in results]):
                    Logger.info("Got Permissions")
                else:
                    Logger.info("Did not accept permissions")
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE], callback)
            DOWNLOADS = f"{primary_external_storage_path}/DL2"
            print(f"\n\n\n\n{DOWNLOADS}\nDL2\nDL3\n\n")
            if not os.path.exists(DOWNLOADS):
                os.mkdir(f"{DOWNLOADS}")
                Logger.info("Permissions accepted")


'''     END OF FILE     '''

if __name__ == "__main__":
    FaApp().run()
