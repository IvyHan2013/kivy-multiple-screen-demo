'''
Showcase of Kivy Features
=========================

'''

from kivy.app import App
from os.path import dirname, join
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.animation import Animation
import screens


class ShowcaseApp(App):
    index = NumericProperty(-1)
    current_title = StringProperty()
    screen_names = ListProperty([])
    hierarchy = ListProperty([])

    def build(self):
        self.title = 'hello world'
        self.screens = {}
        self.available_screens = screens.__all__
        self.screen_names = self.available_screens
        self.go_next_screen()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def on_current_title(self, instance, value):
        self.root.ids.spnr.text = value

    def go_previous_screen(self):
        self.index = (self.index - 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        if screen.name != sm.current:
            sm.switch_to(screen, direction='right')
            self.current_title = screen.name

    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        print self.index
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        if screen.name != sm.current:
            sm.switch_to(screen, direction='left')
            self.current_title = screen.name

    def go_screen(self, idx):
        self.index = idx
        self.root.ids.sm.switch_to(self.load_screen(idx), direction='left')

    def go_hierarchy_previous(self):
        ahr = self.hierarchy
        if len(ahr) == 1:
            return
        if ahr:
            ahr.pop()
        if ahr:
            idx = ahr.pop()
            self.go_screen(idx)

    def load_screen(self, index):
        if index in self.screens:
            return self.screens[index]
        print self.available_screens[index]
        screen = getattr(screens, self.available_screens[index])()
        self.screens[index] = screen
        return screen


if __name__ == '__main__':
    ShowcaseApp().run()
