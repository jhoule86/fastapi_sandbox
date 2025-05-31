from fastapi import FastAPI
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
def poster(req: TransactionData):
    print(f'someone sent {req}')
    return req