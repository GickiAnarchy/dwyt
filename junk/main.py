#!etc/bin/python3.10

""" CORE IMPORTS """
import os
import time
import random

""" KIVY IMPORTS """
import kivy
#   Main App
from kivy.app import App
#   Base Window
from kivy.core.window import Window, WindowBase
#   Base Widget
from kivy.uix.widget import Widget
#   Clock
from kivy.clock import Clock
#   Canvas
from kivy.graphics import Canvas, Color, Rectangle
#   Layouts
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
#   User Interactive Widgets
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
#   Properties
from kivy.properties import ObjectProperty,StringProperty,ListProperty,BooleanProperty,NumericProperty
#   Misc Kivy
from kivy.logger import Logger
from kivy.base import EventLoop
from kivy.config import Config

''' KivyMD '''
import kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField

''' 3rd PARTY MODULES '''
#from pytube import YouTube, Search
#from fa_tube import Tube, TRACK_7


""" SETTINGS """
Config.set('graphics', 'resizable', True)
# Config.set('graphics', 'height', 300)
# Config.set('graphics', 'width', 500)


''' pytube YouTube Widget '''
class YouTubeWidget(RelativeLayout):
    pass

class Screen_One(Screen):
    def __init__(self, **kwargs):
        super(Screen_One, self).__init__(**kwargs)



class FA_Screen(Screen):
    def __init__(self, **kwargs):
        super(FA_Screen, self).__init__(**kwargs)
        l1 = MDLabel(text='Hello', halign='center', theme_text_color='Custom',
                     text_color=(0.5,0,0.5,1), font_style='Caption')

        name = MDTextField(text='Enter Name', pos_hint={'center_x':0.8,'center_y':0.8},
                           size_hint_x = None, width=100)

        btn = MDRectangleFlatButton(text='Submit', pos_hint={'center_x':0.5,'center_y':0.3},
                                    on_release=self.btnfunc)

        self.add_widget(l1)
        self.add_widget(name)
        self.add_widget(btn)

    def btnfunc(self, obj):
        print('Button has been pressed\n' + type(obj))




class MainWindow(BoxLayout):
    yt = ObjectProperty(YouTubeWidget)
    def __init__(self,**kwargs):
        super(MainWindow,self).__init__(**kwargs)
        #self.youtube = Tube(TRACK_7)
        #self.yt = YouTubeWidget(yt=self.youtube)
        #self.add_widget(self.yt)
            

class MainApp(MDApp):
    def build(self):
        return FA_Screen()


if __name__ == "__main__":
    MainApp().run()