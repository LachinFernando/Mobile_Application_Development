from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

KV = """
MyGLayout:
    orientation:'vertical'
    size:root.width,root.height
    spacing:20
    padding:20
    Label:
        text:'Hello name!!'  
"""
class Home(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Home(name = 'home'))

class MainApp(MDApp):

    def Build(self):
        self.help_string = Builder.load_string(KV)
        return self.help_string

MainApp().run()