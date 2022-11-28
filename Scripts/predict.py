import requests
import json


def get_prediction(data={"PassengerId":446,"Pclass":3,"Name":"Hello","Sex":"male","Age":40.21,"SibSp":0,"Parch":0,"Fare":256.1646,"Embarked":"S"}):
            url = 'https://askai.aiclub.world/fe295194-8859-440d-8b57-29a079b633ad'
            r = requests.post(url, data=json.dumps(data))
            response = getattr(r,'_content').decode("utf-8")
            response = json.loads(response)
            response = json.loads(response['body'])
            response = response['predicted_label']
            return response

pr = get_prediction()
print(pr)