#!/usr/bin/dwyt

import certifi
import json
import os
import certifi
import requests
import kivy
import pytube
from pytube import YouTube, Search
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
from kivy.utils import platform
from kivy.logger import Logger
from kivy.config import Config
import ptube
from ssltest import TestApp

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
        self.p
        self.title = "title"
        self.author = "channel"
        self.length = "0"
        self.url = "None"
        if self.check_exists():
            self.ids.yt_btn.disabled = True

    def get_yt(self):
        if self.url != None:
            return ptube.Get_YT(self.url)

    def dl_this(self):
        Logger.info("attempting download")
        if self.check_exists():
            self.ids.yt_btn.disabled = True
            return False
        obj = aYouTube(self.get_yt())
        if self.check_exists():
            self.yt_btn.disabled = True
            return False
        Logger.info("downloaded")
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

    # def add_data(self, new_data):
    #     self.yt_data = [{"title":i.title, "author":i.author,"url":i.watch_url,
    #                      "length":str(format(i.length / 60, ".2f"))} for i in new_data]

    def add_data(self, new_data):
        self.yt_data = [{"title":t, "author":a, "url":u} for t,a,u in new_data]

##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class MainBox(BoxLayout):

    def do_it(self):
        txt = self.ids.search_in.text
        res = ptube.Do_Search(txt)
        self.ids.yts.add_data(res)
        # txt = self.ids.search_in.text
        # self.ids.search_in.text = "TRIED"
        # if txt in (None, ""):
        #     lst = [YouTube(T7)]
        #     self.ids.yts.add_data(lst)
        #     return False
        # sch = Search(txt)
        # lst = sch.results
        # self.ids.yts.add_data(lst)
        # return True


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class DWYTApp(App):
    def build(self):
        Logger.info("Start: Started App")
        return MainBox()




#PYTUBE WRAPPER FOR KIVY GUI
#gui :kivy_main

#TODO
'''
    - Create a container to handle many aYouTube objects
    - Create func(poss class) outside of aYouTube class to pass playlists to aYT container
    
'''

dl_dir = os.path.join(os.path.dirname(__file__), "Downloads")

T7 = "https://youtu.be/R44K3tUFh60"
magick_pl = "https://youtube.com/playlist?list=PLXS7fy2pHgKch6L4xtvybDqxo4tVWAoKK"


#######################################
class aYouTube():
    def __init__(self, yt = ""):
        ''' aYT Initialization '''
        self.YouTube = None

        self.title = ""
        self.url = ""
        self.thumbnail = None
        self.video_id = None
        self.length = None
        self.author = ""
        self.channel_url = ""
        self.channel_id = None
        self.views = 0
        self.desc = ""

        if isinstance(yt, YouTube):
            self.add_youtube(yt)
        if isinstance(yt, str):
            if yt.startswith("https"):
                self.add_youtube(YouTube(yt))

        self.var_dict = {}
        self.var_list = [self.title,self.url,self.thumbnail,self.video_id,self.length,self.author,self.channel_url,self.channel_id,self.views,self.desc]


#    Overrides
    def __dict__(self):
        if len(self.var_dict.keys()) <= 0:
            self.var_dict = {
                "title" : self.title,
                "url" : self.url,
                "thumbnail" : self.thumbnail,
                "video_id" : self.video_id,
                "length" : self.length,
                "author" : self.author,
                "channel_url" : self.channel_url,
                "channel_id" : self.channel_id,
                "views" : self.views,
                "desc" : self.desc}
        return self.var_dict


    def __repr__(self):
        return self.title


    def __str__(self):
        return self.title


#    Adding YouTube
    def add_youtube(self, yt):
        self.YouTube = yt
        self.title = yt.title
        self.url = yt.watch_url
        self.thumbnail = yt.thumbnail_url
        self.video_id = yt.video_id
        self.length = yt.length
        self.author = yt.author
        self.channel_url = yt.channel_url
        self.channel_id = yt.channel_id
        self.views = yt.views
        self.desc = yt.description


#    Downloading and OAuth
    def set_oauth(self, allow=True):
        self.YouTube.use_oauth = True
        self.YouTube.allow_oauth_cache = allow


    def download_video(self, outdir = dl_dir):
        yt = self.YouTube
        video = (
            yt.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
            .download())
        try:
            out_file = video.download(output_path=outdir)
        except Exception as e:
            print(type(e))
            print(e)
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp4"
        os.rename(out_file, new_file)
        Logger.info(f"{new_file}")
        return True


    def download_audio(self, outdir = dl_dir):
        yt = self.YouTube
        audio = yt.streams.get_audio_only()
        try:
            out_file = audio.download(output_path=outdir)
        except Exception as e:
            print(type(e))
            print(e)
            return False
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        Logger.info(f"{new_file}")
        return True


    def read_downloads(self):
        audio_files = []
        video_files = []
        for f in os.listdir(dl_dir):
            if f.endswith(".mp3"):
                audio_files.append(f)
            if f.endswith(".mp4"):
                video_files.append(f)
        return audio_files.extend(video_files)



##    PROPERTIES    ##
    @property
    def YouTube(self):
    	return self._YouTube
    @YouTube.setter
    def YouTube(self, newYouTube):
    	self._YouTube = newYouTube

    @property
    def title(self):
    	return self._title
    @title.setter
    def title(self, newtitle):
    	self._title = newtitle
    
    @property
    def url(self):
    	return self._url
    @url.setter
    def url(self, newurl):
    	self._url = newurl
    
    @property
    def thumbnail(self):
    	return self._thumbnail
    @thumbnail.setter
    def thumbnail(self, newthumbnail):
    	self._thumbnail = newthumbnail
    
    @property
    def video_id(self):
    	return self._video_id
    @video_id.setter
    def video_id(self, newvideo_id):
    	self._video_id = newvideo_id
    
    @property
    def length(self):
    	return self._length
    @length.setter
    def length(self, newlength):
    	self._length = newlength
    
    @property
    def author(self):
    	return self._author
    @author.setter
    def author(self, newauthor):
    	self._author = newauthor
    
    @property
    def channel_url(self):
    	return self._channel_url
    @channel_url.setter
    def channel_url(self, newchannel_url):
    	self._channel_url = newchannel_url
    
    @property
    def channel_id(self):
    	return self._channel_id
    @channel_id.setter
    def channel_id(self, newchannel_id):
    	self._channel_id = newchannel_id
    
    @property
    def views(self):
    	return self._views
    @views.setter
    def views(self, newviews):
    	self._views = newviews
    
    @property
    def desc(self):
    	return self._desc
    @desc.setter
    def desc(self, newdesc):
    	self._desc = newdesc



#######################################


#######################################
list_dir = os.path.join(os.path.dirname(__file__), "lists")

class YT_List():
    def __init__(self):
        self.listname = ""
        self.customlist = []
        self.length = 0


    def add(self, ayt: aYouTube):
        t, i, a = ayt.title, ayt.id, ayt.author
        for vid in self.customlist:
            if t == vid.title and i == vid.id and a == vid.author:
                print(f"{vid.title} already in list")
                return False
        self.customlist.append(ayt)
        self.update()


    def name_list(self, newname):
        if newname in (None, ""):
            return False
        self.listname = newname
        return True


    def save_list(self):
        if self.listname == "":
            return False
        else:
            with open(self.listname + ".txt", "w") as file:
                for item in self.customlist:
                    file.write(item.url)


    def load_list(self, lfile):
        pass


    def update(self):
        self.length = len(self.customlist)


    @property
    def listname(self):
        return self._listname
    @listname.setter
    def listname(self, new_listname):
        self._listname = new_listname



#######################################
#    DEBUG VARS & FUNCS
global fempt
fempt = aYouTube()
track7 = YouTube(T7)

def makeEmpty():
    fempt = aYouTube()

def fillEmpty(f: aYouTube = fempt):
    fempt = f.add_youtube(track7)

def showdebug():
    d = dict(fempt)
    for k in d.keys():
        v = d.get(k)
        print(f"{k}\t---\t{v}")


    
#######################################
#    Pre-Setup
def presetup():
    if not os.path.isdir(dl_dir):
        os.makedirs(dl_dir)
    if not os.path.isdir(list_dir):
        os.makedirs(list_dir)
    return






##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
if __name__ == "__main__":
    try:
        TestApp().test_requests()
        TestApp().test_urllib()
    except:
        Logger.info("except in namemain")
    presetup()
    DWYTApp().run()
