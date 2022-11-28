from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivymd.app import MDApp
from plyer import filechooser
import requests
import base64

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
        MDTopAppBar:
            title: "Cats & Dog Classifier"
            right_action_items: [['android', lambda x:x], ['language-python',lambda x:x]]
        MDBoxLayout:
            orientation: "vertical"
            padding: 50
            spacing: 20
            MDLabel:
                text: "Cats and Dogs Classifier"
                font_style: "H3"
                halign: 'center'
            
            MDRaisedButton:
                text: "Prediction Dashboard"
                md_bg_color: "red"
                pos_hint: {"center_x":0.5}
                size_hint: (0.3,0.2)
                font_size:15
                on_press: root.manager.current = 'prediction'
<Prediction>:
    name: 'prediction'

    MDBoxLayout:
        orientation:'vertical'

        MDTopAppBar:
            title: "Prediction Dashboard"
            right_action_items: [['android', lambda x:x], ['language-python',lambda x:x]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: 10
            spacing: 10
            Image:
                id: selected_image
                pos_hint: {"center_x":0.5}
            MDLabel:
                id: prediction_label
                text: ""
                halign: "center"
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 10
                padding: 10

                MDRaisedButton:
                    text: "Upload"
                    size_hint: (0.2,0.3)
                    on_press: app.file_chooser()

                MDRaisedButton:
                    text: "Predict"
                    size_hint: (0.2,0.3)
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
            self.root.ids.prediction_screen.ids.selected_image.source = selection[0]
            self.path_selection = selection[0]
            if self.message:
                self.help_string.get_screen('prediction').ids.prediction_label.text = ""
            return self.path_selection


    def prediction(self):
        def get_prediction(image_data):
            url = 'https://askai.aiclub.world/45f585a9-75af-4bdc-ac7a-5e872c49be8f'
            r = requests.post(url, data=image_data)
            response = r.json()['predicted_label']
            print(response)
            return response
        
        if not self.path_selection:
            self.message = "Please Upload an Image"
            self.help_string.get_screen('prediction').ids.prediction_label.text = self.message
        else:
            with open(self.path_selection,'rb') as image:
                payload = base64.b64encode(image.read())
            response = get_prediction(payload)
            self.response_message = "This is a picture of a {}".format(response[:-1])
            self.help_string.get_screen('prediction').ids.prediction_label.text = self.response_message

MainApp().run()
