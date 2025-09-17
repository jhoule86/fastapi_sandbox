from time import sleep
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from .basic_routes import read_root

router = APIRouter(prefix='/time')

@router.api_route("/hang/{sec}")
async def hang(sec: int):
    sleep(sec)
    return read_root()

@router.api_route("/redirecthang/{sec}")
async def redirecthang(sec: int):
    sleep(sec)
    return RedirectResponse("/json/sample")
