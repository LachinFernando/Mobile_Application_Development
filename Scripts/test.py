from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

KV = """
MDFloatLayout:
    MDLabel:
        text: "START"
        font_size: 36
    MDLabel:
        text: "Middle"
        font_size: 36
    MDLabel:
        text: "Finish"
        font_size: 36
        pos_hint: {"center_x":0.5}
"""

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
        
    def on_start(self):
        self.root.current = "main"

if __name__ == "__main__":
    MainApp().run()