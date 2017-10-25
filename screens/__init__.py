from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty

class ShowcaseScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(ShowcaseScreen, self).add_widget(*args)

from togglebutton import ToggleButtonScreen

__all__ = ['ToggleButtonScreen']
