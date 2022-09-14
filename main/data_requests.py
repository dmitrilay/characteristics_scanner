import json
import requests
from requests.auth import AuthBase


def sending_data():
    url = 'http://127.0.0.1:8000/spec/add-characteristic-ajax/'
    _r = requests.get(url)
    _d = json.loads(_r.text)
    return (_d)


class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r


token = "fjwoapfjow@204diojwa!24dkapwojfjjf22401jdwa190jd(odwa"


def sending_spec(obj):
    _json = json.dumps(obj)
    url = 'http://127.0.0.1:8000/spec/add-characteristic-ajax/'
    _r = requests.post(url, auth=TokenAuth(token), data={'data': _json})


# sending_data()
# sending_spec()
