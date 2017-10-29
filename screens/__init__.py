from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.lang import Builder

Builder.load_string('''
<ShowcaseScreen>:
    ScrollView:
        do_scroll_x: False
        do_scroll_y: False if root.fullscreen else (content.height > root.height - dp(16))
        AnchorLayout:
            size_hint_y: None
            height: root.height if root.fullscreen else max(root.height, content.height)
            GridLayout:
                id: content
                cols: 1
                spacing: '8dp'
                padding: '8dp'
                size_hint: (1, 1) if root.fullscreen else (.8, None)
                height: self.height if root.fullscreen else self.minimum_height
''')

class ShowcaseScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(ShowcaseScreen, self).add_widget(*args)

from togglebutton import ToggleButtonScreen
from togglebutton2 import ToggleButtonDupScreen
from visHome import VisHomeScreen
from radio import RadioScreen
from dpstat import DPStatScreen
from conInfo import ConInfoScreen
from mobInfo import MobInfoScreen
from dvSer import DVSerScreen 

__all__ = ['ToggleButtonScreen', 'ToggleButtonDupScreen', 'VisHomeScreen',\
            'RadioScreen','DPStatScreen','ConInfoScreen','MobInfoScreen','DVSerScreen']
