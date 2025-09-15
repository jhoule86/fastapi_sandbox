Feature: The basic endpoints

  Scenario: calling the get endpoint
    Given url 'http://localhost:8000/get'
    When method get
    Then status 200
    And match response == 
    """
    {
    "status": "new",
    "data": "this is the original data"
    }
    """

  Scenario: calling the post endpoint
    Given def payload = {"status":"new","data":"This is something new for you!"}
    And url 'http://localhost:8000/post'
    And request payload
    When method post
    Then status 200
    And match response == payload

  Scenario: getting the sample data
    Given url 'http://localhost:8000/json/sample'
    When method get
    Then status 200
    And match response == 
    """
   { 
    "status": "new",
    "items": [
        "one",
        "two",
        "four"
    ],
    "data": "foo"
    }
    """

  Scenario Outline: matching a request
    Given url 'http://localhost:8000/match/sample'
    And request {"status":"new", "items":["one","two","three"],"data":"foo"}
    And headers {"content-type":"application/json","myHeader":"myValue"}
    When method <METHOD>
    Then status 200
    And assert response.status == 'passed'
    And assert response.data == '[]'
        Examples:
            | METHOD |
            | post   |
            | put    | 
    
  Scenario Outline: failure when matching a request
    Given url 'http://localhost:8000/match/sample'
    And request {"status":"bad", "items":["harry","larry","mo"],"data":"bar"}
    And headers {"content-type":"application/json","myHeader":"wrongValue"}
    When method <METHOD>
    Then status 400
    And assert response.status == 'failed'
    And assert response.data != '[]'
        Examples:
            | METHOD |
            | post   |
            | put    | 
