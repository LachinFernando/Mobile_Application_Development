from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivymd.app import MDApp
import kivymd
print(kivymd.__version__)

KV = """
ScreenManager:
    Home:
        id:home_screen
    Menu:
        id:menu_screen
<Home>:
    name:'home'
    MDBoxLayout:
        orientation:"vertical"
        MDTopAppBar:
            title: "Home Screen"
        MDBoxLayout:
            orientation: "vertical"
            padding: 10
            spacing: 10
            Image:
                source: "assets/dice_1.png"
            MDRaisedButton:
                text:"Menu Screen"
                pos_hint:{"center_x":0.5}
                on_press: root.manager.current = 'menu'
<Menu>:
    name: 'menu'
    MDBoxLayout:
        orientation:"vertical"
        MDTopAppBar:
            title: "Menu Screen"
        MDBoxLayout:
            padding: 10
            spacing: 10
            orientation: "vertical"
            
            
"""

class Home(Screen):
    pass

class Menu(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name = 'home'))
        sm.add_widget(Menu(name = 'menu'))
        self.string = Builder.load_string(KV)
        return self.string

MainApp().run()