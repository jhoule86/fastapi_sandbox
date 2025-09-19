from time import sleep
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from .basic_routes import read_root

router = APIRouter(prefix="/time")


@router.api_route("/hang/{sec}")
async def hang(sec: int):
    """
    Wait for the prescribed amount of seconds,
    then return a basic response
    """

    sleep(sec)
    return read_root()


@router.api_route("/redirecthang/{sec}")
async def redirecthang(sec: int):
    """
    Wait for the prescribed amount of seconds,
    then redirect to an internal endpoint that returns a basic response
    """

    sleep(sec)
    return RedirectResponse("/json/sample")
