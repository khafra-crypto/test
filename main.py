from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.utils import get_color_from_hex


class BlueScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = get_color_from_hex("#2196F3")  # أزرق

        self.button = MDButton(
            MDButtonText(text="Go to first Screen"),
            style="filled",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.add_widget(self.button)


class RedScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = get_color_from_hex("#F44336")  # أحمر

        self.button = MDButton(
            MDButtonText(text="Go to second Screen"),
            style="filled",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.add_widget(self.button)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"

        self.screen_manager = MDScreenManager()

        self.blue_screen = BlueScreen(name="blue")
        self.red_screen = RedScreen(name="red")

        self.blue_screen.button.on_release = lambda: self.change_screen("red")
        self.red_screen.button.on_release = lambda: self.change_screen("blue")

        self.screen_manager.add_widget(self.blue_screen)
        self.screen_manager.add_widget(self.red_screen)

        return self.screen_manager

    def change_screen(self, screen_name):
        self.screen_manager.current = screen_name


if __name__ == "__main__":
    MainApp().run()