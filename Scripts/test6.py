from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest

import certifi as cf
import json

KV = """
ScreenManager:
    Home:
        id:home_screen
    Predictions:
        id:prediction_screen

<Home>:
    name: "home"
    MDBoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            title: "Home Screen"
        MDBoxLayout:
            orientation: "vertical"
            padding: 15
            spacing: 10
            Image:
                source:"assets/dice_1.png"
                size_hint: (0.5,0.5)
                pos_hint: {"center_x":0.5}
            MDRoundFlatButton:
                text:"Prediction Dashboard"
                on_press: root.manager.current = "prediction"
                pos_hint: {"center_x":0.5}
                size_hint: (0.3,0.05)
<Predictions>:
    name: "prediction"
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Preiction DashBoard"
        MDBoxLayout:
            orientation: "vertical"
            padding: 5
            spacing: 10
            MDLabel:
                text: "Welcome to the prediction Dashboard"
                font_style: "H3"
                halign: "center"
                pos_hint: {"center_x":0.5}
            MDLabel:
                id:label_one
                text: ""
                halign: "center"
                pos_hint: {"center_x":0.5}
                font_style: "H1"
            MDRoundFlatButton:
                text: "Predict"
                on_press: app.predict()
                pos_hint: {"center_x":0.5}
"""

class Home(Screen):
    pass

class Predictions(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Home(name = "home"))
sm.add_widget(Predictions(name = "prediction"))

class MainApp(MDApp):
    def build(self):
        self.string = Builder.load_string(KV)
        return self.string
    
    def predict(self):
        data={"PassengerId":446,"Pclass":3,"Name":"Hello","Sex":"male","Age":40.21,"SibSp":0,"Parch":0,"Fare":256.1646,"Embarked":"S"}
        data=json.dumps(data)
        url = 'https://askai.aiclub.world/fe295194-8859-440d-8b57-29a079b633ad'
        self.request = UrlRequest(url, on_success=self.res, req_body= data, ca_file=cf.where(), verify=True )
    
    def res(self, *args):
        self.data = self.request.result
        response = json.loads(self.data['body'])
        response = response['predicted_label']
        print(response)
        self.string.get_screen("prediction").ids.label_one.text = str(response)
        

MainApp().run()

# def get_prediction(data={"PassengerId":446,"Pclass":3,"Name":"Hello","Sex":"male","Age":40.21,"SibSp":0,"Parch":0,"Fare":256.1646,"Embarked":"S"}):
#             url = 'https://askai.aiclub.world/fe295194-8859-440d-8b57-29a079b633ad'
#             r = requests.post(url, data=json.dumps(data))
#             response = getattr(r,'_content').decode("utf-8")
#             response = json.loads(response)
#             response = json.loads(response['body'])
#             response = response['predicted_label']
#             return response

#         answer = get_prediction()
#         self.string.get_screen('prediction').ids.label_one.text = str(answer)