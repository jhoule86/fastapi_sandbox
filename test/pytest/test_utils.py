from models.cannedjson import CannedJson
from utils.jsonloader import load_cannedjson

def test_load_sample():
    """
    Tests that the sample is loaded correctly 
    into the internal representation of data and/or headers
    """
    
    canned = load_cannedjson("sample")

    assert isinstance(canned, CannedJson)
    
    assert canned.headers
    assert isinstance(canned.headers, dict)
    assert canned.headers['content-type'] == 'application/json'
    assert canned.headers['myHeader'] == 'myValue'

    assert canned.payload
    assert isinstance(canned.payload, dict)

    assert canned.payload['status'] == 'new'
    assert canned.payload['items'][0] == 'one'
    assert canned.payload['items'][1] == 'two'
    assert canned.payload['items'][2] == 'three'
    assert canned.payload['data'] == 'foo'
