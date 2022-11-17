#!etc/bin/python3.10

import os
import datetime

""" KIVY IMPORTS """
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
#   Screens and Pages
from kivy.uix.screenmanager import Screen,ScreenManager,RiseInTransition
#   User Interactive Widgets
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
#   Properties
from kivy.properties import ObjectProperty, StringProperty, ListProperty, BooleanProperty, NumericProperty
#   Misc Kivy
from kivy.logger import Logger
from kivy.base import EventLoop
from kivy.config import Config

''' KivyMD '''
# import kivymd
# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen, MDScreen
# from kivymd.uix.label import MDLabel
# from kivymd.uix.button import MDTextButton
# from kivymd.uix.button import MDRectangleFlatButton
# from kivymd.uix.list import MDList
# from kivymd.uix.card import MDCard
# from kivymd.uix.textfield import MDTextField


class Front_Screen(Screen):
    pass

class Search_Screen(Screen):
    pass

class About_Screen(Screen):
    pass


class Page_Master(ScreenManager):
    def __init__(self, **kwargs):
        super(Page_Master, self).__init__(**kwargs)
        self.transition=RiseInTransition()
        self.add_widget(Front_Screen(name='front_screen'))
        self.add_widget(Search_Screen(name='search_screen'))
        self.add_widget(About_Screen(name='about_screen'))

    def to_home(self, obj):
        self.current_screen='front_screen'


class Fa_Window(BoxLayout):
    pmaster=ObjectProperty(None)

class FaApp(App):
    def build(self):
        Logger.info("\n\tstarting FaApp")
        return Fa_Window()


'''     END OF FILE     '''

if __name__ == "__main__":
    FaApp().run()