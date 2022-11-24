""" Down With YouTube :: Main.py || email: fatheranarchy@programmer.net """

import os

''' PyTube '''
from pytube import YouTube

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
from kivy.uix.screenmanager import Screen,ScreenManager,RiseInTransition,ShaderTransition
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

Config.set("graphics","resizable", True)
EventLoop.ensure_window()
window = EventLoop.window

DOWNLOADS = "Downloads/"
if not os.path.exists(DOWNLOADS):
    os.mkdir(DOWNLOADS)


class Front_Screen(Screen):
    def do_popup(self):
        self.popup = Popup(title="ABOUT", content=Label(text="Made by:\nGickiAnarchy\nEmail:fatheranarchy@programmer.net"), size_hint=(0.6, 0.6))
        self.popup.open()


class Search_Screen(Screen):
    pass


class Download_Screen(Screen):
    dl_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Download_Screen, self).__init__(**kwargs)
        self.dl_input = self.ids['dl_input']

    def download(self,format = ""):
        url = self.dl_input.text
        try:
            y = YouTube(url)
            self.pop = Popup(title="Download", content=Label(f"{y.title}\nPosted By:\n{y.author}"))
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
        self.transition=ShaderTransition()
        self.add_widget(Front_Screen(name='front_screen'))
        self.add_widget(Search_Screen(name='search_screen'))
        self.add_widget(Download_Screen(name='download_screen'))

    def to_home(self):
        self.current='front_screen'


class Fa_Window(RelativeLayout):
    pmaster=ObjectProperty(None)


    # def __init__(self, **kwargs):
    #     super(Fa_Window, self).__init__(**kwargs)
    #     self.size_hint=(None,None)


class FaApp(App):
    win = ObjectProperty(None)


    def build(self):
        Logger.info("\n\tstarting FaApp")
        return Fa_Window()

    def on_start(self):
        super(FaApp, self).on_start()
        self.win = window
        self.size = self.win.size


'''     END OF FILE     '''

if __name__ == "__main__":
    FaApp().run()