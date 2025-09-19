from os.path import dirname, realpath
from json import loads as json_loads

from models.cannedjson import CannedJson

_base_dir = dirname(dirname(realpath(__file__)))
_bin_dir = realpath(f"{_base_dir}/bin")


def load_cannedjson(name: str) -> CannedJson:
    dir = realpath(f"{_bin_dir}/response/{name}")

    payload_file_name = realpath(f"{dir}/payload.json")
    payload_file = open(payload_file_name)
    if not payload_file:
        raise FileNotFoundError(f"no json payload found for {name}")
    payload = json_loads(payload_file.read())

    headers = None
    headers_file_name = realpath(f"{dir}/headers.json")
    headers_file = open(headers_file_name)
    if headers_file:
        headers = json_loads(headers_file.read())

    return CannedJson(payload=payload, headers=headers)
