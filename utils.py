from os import path as os_path
from json import loads as json_loads

_pwd = os_path.dirname(os_path.realpath(__file__))

class CannedJson():
    def __init__(self, payload, headers = None):
        self.payload = payload
        self.headers = headers

def load_canned_json(name: str) -> CannedJson:
    payload_file_name = os_path.realpath(f'{_pwd}/bin/response/{name}/payload.json')
    payload_file = open(payload_file_name)
    if not payload_file:
        raise FileNotFoundError(f'no json payload found for {name}')
    payload = json_loads(payload_file.read())

    headers = None
    headers_file_name = os_path.realpath(f'{_pwd}/bin/response/{name}/headers.json')
    headers_file = open(headers_file_name)
    if headers_file:
        headers = json_loads(headers_file.read())
    
    return CannedJson(payload, headers)
