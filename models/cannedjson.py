from typing import Dict, List

class CannedJson():
    def __init__(self, payload: str | List | Dict, headers: Dict | None = None):
        self.payload = payload
        self.headers = headers
