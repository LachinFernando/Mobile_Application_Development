from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivymd.app import MDApp

KV = """
ScreenManager:
    Home:
        id:home_screen
<Home>
    name: 'home'
    MDBoxLayout:
        orientation:"vertical"
        FitImage:
            source: "assets\catsdogs.jpeg"
    
        MDRaisedButton:
            text:"This is an Image"
            size_hint:(0.5,0.2)
            pos_hint: {"center_x":0.5}
"""

class Home(Screen):
    pass

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(Home(name = 'home'))

class MainApp(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.help_string = Builder.load_string(KV)
        return self.help_string
MainApp().run()