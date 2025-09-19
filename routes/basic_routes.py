from fastapi import APIRouter, Request

from models.transactiondata import TransactionData

router = APIRouter()


@router.get("/")
def read_root():
    """
    Default endpoint from fastapi
    """

    return {"Hello": "World"}


@router.get("/get")
def getter():
    """
    Get a simple TransactionData
    """

    return TransactionData(status="new", data="this is the original data")


@router.post("/post")
async def poster(transaction: TransactionData, request: Request):
    """
    Echoes a POSTed TransactionData
    """
    print(f"someone sent {transaction}")
    print(f"with headers {request.headers}")
    return transaction


@router.api_route("/printer", methods=["POST", "PUT"])
async def printer(request: Request):
    """
    Prints the raw request body and headers out to console
    """
    body = await request.body()
    print(f"someone sent {body}")
    print(f"with headers {request.headers}")

    return TransactionData(
        status="done", data="look at the standard output stream for details"
    )
