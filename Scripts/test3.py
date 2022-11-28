from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivymd.app import MDApp
import random

KV = """
ScreenManager:
    Home:
        id: home_screen
<Home>:
    name: "home"
    BoxLayout:
        orientation: "vertical"
        padding: 10
        spacing: 10
        MDTopAppBar:
            title: "Test APP"
        Image:
            id: img
            source: "assets/dice_1.png"
            size_hint: (0.4,0.4)
            pos_hint:{"center_x":0.5,"center_y":0.5}
        MDRoundFlatButton:
            id: button1
            text: "Roll the Dice"
            text_color: "black"
            pos_hint: {"center_x":0.5, "center_y":0.3}
            on_press: app.roll()
"""

class Home(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Home(name = 'home'))

class MainApp(MDApp):
    def build(self):
        self.string = Builder.load_string(KV)
        return self.string
    def roll(self):
        list1 = ["dice_{}.png".format(i) for i in range(1,7)]
        name = random.choice(list1)
        path_name = "assets/" + name
        self.root.ids.home_screen.ids.img.source = path_name


MainApp().run()