import requests
import json
import jsonpath


def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/Users/KriKumar/Documents/PytestLearning/AutomationCases/RequestJson.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)