import certifi
import os
import kivy
from pytube import YouTube, Search
import pytube
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import ObjectProperty, StringProperty,ListProperty
from kivy.logger import Logger
from kivy.config import Config
from ayoutube import aYouTube, T7
os.environ["SSL_CERT_FILE"] = certifi.where()

Config.set('graphics', 'resizable', True)

dl_dir = os.path.join(os.path.dirname(__file__), "Downloads")


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class YT_Header(BoxLayout):
    def __init__(self, **kwargs):
        super(YT_Header, self).__init__(**kwargs)
        logo = Image(source = "images/down_logo.png", allow_stretch = False, keep_ratio = True)
        logo.size_hint_y = 0.75
        logo.pos_hint = {"center_x": 0.5}
        self.add_widget(logo)


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class YT_Widget(BoxLayout):
    title = StringProperty()
    author = StringProperty()
    length = StringProperty()
    url = StringProperty()
    yt_btn = ObjectProperty(Button)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.info("USE: YT_Widget")
        self.title = "title"
        self.author = "channel"
        self.length = "0"
        self.url = "None"
        if self.check_exists():
            self.ids.yt_btn.disabled = True

    def get_yt(self):
        if self.url != None:
            yt = YouTube(self.url)
            ayt = aYouTube(yt)
            return ayt

    def dl_this(self):
        if self.check_exists():
            self.ids.yt_btn.disabled = True
            return False
        obj = self.get_yt()
        if self.check_exists():
            self.yt_btn.disabled = True
            return False
        obj.download_audio()

    def check_exists(self):
        if self.url in (None, ""):
            return False
        if os.path.isfile(f"{dl_dir}/{self.title}.mp3") or os.path.isfile(f"{dl_dir}/{self.title}.mp4"):
            return True
        

##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class Ask(Popup):
    pass


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class YT_List(RecycleView):
    yt_data = ListProperty()

    def add_data(self, new_data):
        self.yt_data = [{"title":i.title, "author":i.author,"url":i.watch_url,
                         "length":str(format(i.length / 60, ".2f"))} for i in new_data]


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class MainBox(BoxLayout):

    def do_it(self):
        txt = self.ids.search_in.text
        if txt in (None, ""):
            lst = [YouTube(T7)]
            self.ids.yts.add_data(lst)
            return False
        else:
            sch = Search(txt)
            lst = sch.results
            self.ids.yts.add_data(lst)
        return True


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class DWYTApp(App):
    def build(self):
        Logger.info("Start: Started App")
        return MainBox()


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
if __name__ == "__main__":
    DWYTApp().run()
