from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from arabic_reshaper import reshape
from bidi.algorithm import get_display

def fix_arabic_text(text):
    reshaped_text = reshape(text)
    return get_display(reshaped_text)

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label = MDLabel(
            text=fix_arabic_text("مرحبًا بك في تطبيقنا"),
            halign="center",
            font_name="Arial-Regular.ttf",  # تأكد أن الملف موجود بنفس الاسم!
        )
        self.add_widget(label)

class MyApp(MDApp):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    MyApp().run()
