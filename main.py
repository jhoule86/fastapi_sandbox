from os import path as os_path
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from json import loads as json_loads

_pwd = os_path.dirname(os_path.realpath(__file__))

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

@app.get("/json/{name}")
def get_json(name):
    payload_file_name = os_path.realpath(f'{_pwd}/bin/response/{name}/payload.json')
    payload_file = open(payload_file_name)
    if not payload_file:
        raise TypeError(f'no json payload found for {name}')
    payload = payload_file.read()

    headers = None
    headers_file_name = os_path.realpath(f'{_pwd}/bin/response/{name}/headers.json')
    headers_file = open(headers_file_name)
    if headers_file:
        headers = json_loads(headers_file.read())

    return JSONResponse(content=payload, headers=headers)
