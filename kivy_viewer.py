from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # set app theme
        self.theme_cls.primary_palette = "Blue"  # set app primary palette

        return Builder.load_file('weather_card.kv')


if __name__ == '__main__':
    MainApp().run()
