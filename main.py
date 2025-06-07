
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from bidi.algorithm import get_display
import arabic_reshaper

def fix_arabic_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

class MyApp(MDApp):
    def build(self):


        return MDLabel(
            text=fix_arabic_text("welcome"),
            halign="center",
            font_name="Amiri-Regular"  # فقط هذا السطر مطلوب لتغيير الخط
        )

if __name__ == "__main__":
    MyApp().run()
