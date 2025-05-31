from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PosterRequest(BaseModel):
    status: str
    input: str | bytes

class PosterResponse(BaseModel):
    status: str
    output: str | bytes


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get")
def getter():
    return {"input": "Something I made"}

@app.post("/post")
def poster(req: PosterRequest):
    print(f'someone sent {req}')
    return PosterResponse(status = req.status, output=req.input)