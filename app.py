from time import strftime
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel


# Window.size = (300, 100)

# Set size of the window on startup
# Config.set('graphics', 'width', '1920')
# Config.set('graphics', 'height', '1080')
# Dynamically


class DragLabel(DragBehavior, Label):
    pass


class Cardzin(DragBehavior, MDCard, RoundedRectangularElevationBehavior):
    pass


class ClockLabel(MDLabel):
    pass


class MainApp(MDApp):
    sw_started = False
    sw_seconds = 0

    def build(self):
        self.theme_cls.theme_style = "Dark"  # set app theme
        self.theme_cls.primary_palette = "Blue"  # set app primary palette

        return Builder.load_file('home.kv')

    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes, _ = divmod(self.sw_seconds, 60)

        self.root.ids.time.text = strftime('%H:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(
        name='Roboto',
        fn_regular='Roboto-Thin.ttf',
        fn_bold='Roboto-Medium.ttf'
    )

    MainApp().run()
