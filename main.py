from fastapi import FastAPI, Request, Response, status
from pydantic import BaseModel

app = FastAPI()

class TransactionData(BaseModel):
    status: str
    data: str | bytes


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get")
def getter():
    return TransactionData(status='new', data='this is the original data')

@app.post("/post")
def poster(transaction: TransactionData, request: Request, response: Response):
    print(f'someone sent {transaction}')
    print(f'with headers {request.headers}')
    #response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return transaction
