from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
import arabic_reshaper
from bidi.algorithm import get_display
from bidi import algorithm
algorithm.use_c_extension = False

class FirstScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        text = "خالد"
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)

        self.add_widget(
            MDRaisedButton(
                text=bidi_text,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_release=self.go_to_second,
                font_name="Amiri-Regular.ttf"  # تأكد أن الخط موجود في مجلد المشروع
            )
        )

    def go_to_second(self, instance):
        self.manager.current = "second"


class SecondScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            MDLabel(
                text="Hello",
                halign="center",
                pos_hint={"center_y": 0.5},
                font_style="H4"
            )
        )


class Khaled(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        return sm


Khaled().run()
