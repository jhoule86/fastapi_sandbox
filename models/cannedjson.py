from typing import Dict, List

from pydantic import BaseModel

class CannedJson(BaseModel):
    payload: str | List | Dict
    headers: Dict | None = None
