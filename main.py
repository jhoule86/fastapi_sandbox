from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from json import dumps as json_dumps, loads as json_loads

from models import TransactionData
from utils import load_canned_json, CannedJson

app = FastAPI()


@app.get("/")
def read_root():
    """
    Default endpoint from fastapi
    """
    
    return {"Hello": "World"}

@app.get("/get")
def getter():
    """
    Get a simple TransactionData
    """
    
    return TransactionData(status='new', data='this is the original data')

@app.post("/post")
async def poster(transaction: TransactionData, request: Request, response: Response):
    """
    Echoes a POSTed TransactionData
    """
    print(f'someone sent {transaction}')
    print(f'with headers {request.headers}')
    return transaction

@app.get("/json/{name}")
def get_json(name: str, request: Request):
    """
    Get a canned json response
    """

    print(f'someone requested the json with name "{name}"')
    print(f'with headers {request.headers}')
    
    try:
        canned_data = load_canned_json(name)
    except Exception as e:
        print(str(e))
        return JSONResponse(content=f'Content not found for name: {name} - {e}', status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content=canned_data.payload, headers=canned_data.headers)

@app.api_route("/match/{name}", methods=["POST", "PUT"])
async def match_json(name, request:Request):
    """
    Check a json request and optionally its headers against stored data
    """

    try:
        canned_data: CannedJson = load_canned_json(name)
    except Exception as e:
        print(e)
        return JSONResponse(content=f'Content not found for name: {name}', status_code=status.HTTP_404_NOT_FOUND)
    
    issues = []
    
    if canned_data.headers:
        for key in canned_data.headers:
            if not key in request.headers:
                issues.append(f'The required header {key} is missing from the request')
            else:                
                expected = canned_data.headers[key]
                actual = request.headers[key]

                # be lenient about charset on incoming content-type
                if key.lower() == 'content-type' and not ';' in expected:
                    semi_loc_actual = actual.find(';')
                    if (semi_loc_actual > 0):
                        actual = actual[:semi_loc_actual]

                if (expected != actual):
                    issues.append(f'The value "{actual}" for the header {key} does not match the expectation of "{expected}"')

    json_sent = await request.json()

    if json_sent != canned_data.payload:
        # TODO: consider providing a diff instead of full values.
        issues.append(f'The payload "{json_sent}" does not match the expected payload of "{canned_data.payload}"')

    status_code = status.HTTP_200_OK
    status_message = 'passed'
    if len(issues) > 0:
        status_code = status.HTTP_400_BAD_REQUEST
        status_message = 'failed'
    return JSONResponse(content=TransactionData(status=status_message, data=json_dumps(issues)).model_dump(), status_code=status_code)

@app.api_route("/printer", methods=["POST", "PUT"])
async def printer(request: Request):
    """
    Prints the raw request body and headers out to console
    """
    body = await request.body()
    print(f'someone sent {body}')
    print(f'with headers {request.headers}')

    return TransactionData(status='done', data='look at the standard output stream for details')
