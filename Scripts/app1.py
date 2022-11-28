from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
from kivy import platform

import certifi as cf
import base64
from plyer import filechooser
import os




if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

os.environ['KIVY_IMAGE'] = 'pil,sdl2'


kV = """

ScreenManager:
    Home:
        id: home_screen
    Prediction:
        id: prediction_screen
<Home>:
    name: 'home'
    MDBoxLayout:
        orientation: "vertical"
        spacing: 10
        MDTopAppBar:
            title: "Cats & Dog Classifier"
            right_action_items: [['android', lambda x:x], ['language-python',lambda x:x]]
        MDBoxLayout:
            spacing: 20
            padding: 10
            orientation: "vertical"
            size_hint:1,0.8
            MDCard:
                radius: 36
                md_bg_color: "grey"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8, .7

                FitImage:
                    source: "assets/dogscats.png"
                    size_hint_y: 1
                    pos_hint: {"top": 1}
                    radius: 36, 36, 0, 0
            
            MDRaisedButton:
                text: "Predictions"
                md_bg_color: "red"
                pos_hint: {"center_x":0.5}
                size_hint: 0.4,0.08
                font_size:15
                on_press: root.manager.current = 'prediction'
<Prediction>:
    name: 'prediction'

    MDBoxLayout:
        orientation:'vertical'

        MDTopAppBar:
            title: "Prediction Dashboard"
            #right_action_items: [['android', lambda x:x], ['language-python',lambda x:x]]
            left_action_items: [['home', lambda x:app.switch()]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: 10
            spacing: 10
            size_hint: 1,0.8
            MDCard:
                radius: 36
                md_bg_color: "grey"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8, .5

                FitImage:
                    id:selected_image
                    source: ""
                    size_hint:1,1
                    pos_hint: {"top": 1}
                    radius: 36, 36, 0, 0
            MDSpinner:
                id: spinner
                size_hint: (0.1,0.1)
                pos_hint: {'center_x': .5, 'center_y': .5}
                active: False
            MDLabel:
                id: prediction_label
                text: ""
                halign: "center"
                size_hint:(1,0.1)
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 10
                padding: 10
                size_hint:(1,0.3)
                

                MDRaisedButton:
                    text: "Upload"
                    on_press: app.file_chooser()
                    size_hint:(0.5,0.3)

                MDRaisedButton:
                    text: "Predict"
                    size_hint:(0.5,0.3)
                    on_press: app.prediction()

"""

class Home(Screen):
    pass

class Prediction(Screen):
    pass

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(Home(name = 'home'))
sm.add_widget(Prediction(name = 'prediction'))

class MainApp(MDApp):

    path_selection = None
    message = None
    response_message = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.help_string = Builder.load_string(kV)
        return self.help_string

    def file_chooser(self):
        if self.response_message:
            self.help_string.get_screen('prediction').ids.prediction_label.text = ""

        filechooser.open_file(on_selection = self.selected)
    
    def selected(self, selection):
        if selection:
            self.path_selection = selection[0]
            self.help_string.get_screen('prediction').ids.prediction_label.text = self.path_selection
            return self.path_selection


    def prediction(self):
        url = 'https://askai.aiclub.world/45f585a9-75af-4bdc-ac7a-5e872c49be8f'
        if not self.path_selection:
            self.message = "Please Upload an Image"
            self.help_string.get_screen('prediction').ids.prediction_label.text = self.message
        else:
            self.root.ids.prediction_screen.ids.selected_image.source = self.path_selection
            self.help_string.get_screen('prediction').ids.spinner.active = True
            with open(self.path_selection,'rb') as image:
                payload = base64.b64encode(image.read())
            self.request = self.request = UrlRequest(url, on_success=self.res, req_body= payload, ca_file=cf.where(), verify=True )
            # if self.request:
            #     self.help_string.get_screen('prediction').ids.spinner.active = False
            
    def res(self, *args):
        self.data = self.request.result
        response = self.data['predicted_label']
        self.response_message = "This is a picture of a {}".format(response[:-1])
        self.help_string.get_screen('prediction').ids.prediction_label.text = self.response_message
        print("Middle")
        self.help_string.get_screen('prediction').ids.spinner.active = False
    
    def switch(self):
        self.root.current = "home"


MainApp().run()
