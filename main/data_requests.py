import json
import requests


def sending_data():
    url = 'http://127.0.0.1:8000/spec/add-characteristic-ajax/'

    # requests.post('https://ch-shop.ru/', data={'key': 'value'})
    # requests.post(url, data={'key': 'value'})
    _r = requests.get(url)
    # print(_r.status_code)
    # print(_r.content)
    _d = json.loads(_r.text)
    # print(type())
    return (_d)


# sending_data()
