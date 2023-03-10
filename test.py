import requests


def res():
    response = requests.get('http://127.0.0.1:5000/power/', params={'x': 3, 'y': 3})
    print(response.text)