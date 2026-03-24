# fastapi_sandbox

**Author:** Jeff Houle (jhoule86@gmail.com)

**Last Update:** 2025-09-17

## Intro

A [fastapi](https://fastapi.tiangolo.com/) app for testing HTTP/REST clients.

## Setup

### Installation

**Notice:** The following examples are for debian-based linux such as Ubuntu and may not reflect the system in use.

1. Install `python3` and the associated `pip` and `venv` packages
    - for ubuntu, the command is:
        ```
        sudo apt install python3 python3-pip python3-venv
        ```
2. Set up a virtual environment at `<project_root>/.venv` for Python, by using `venv`:
    ```
    python3 -m venv .venv
    ```
3. Use [requirements.txt](requirements.txt) to install required dependencies, including the correct `fastapi` executable for the platform:
    ```
    source ./.venv/bin/activate

    pip install -r requirements.txt
    ```

### Canned json

You may want to craft custom json for usage with endpoints like `get` and `match`:
1. Make a copy of the proper directory, using a meaningful name in place of `sample`:
    * Requests: [bin/response/sample](bin/request/sample)
    * Responses:  [bin/response/sample](bin/response/sample)
2. Upload the new `payload.json` file to reflect the json payload to be returned and/or matched
3. Update or remove the new `headers.json` file to reflect the headers to be returned and/or matched

## Running

Use the run script for your platform (**make sure you are using your virtual python environment where fastapi is installed.** You may need to update the execution path!):
* Unix: [run.sh](run.sh)
* Windows: [run.cmd](run(the python path will differ by version/system).cmd)

## Usage

**The included [http_requests/sample.http](http_requests/sample.http) file contains example requests for execution via clients such as the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension for VS Code.**

### endpoint: get

The `get` endpoint returns a simple json response based on a small `TransactionData` model that is implemented via pydantic.

### endpoint: post

The `post` endpoint echoes a simple json request that is expected to match the schema of the `TransactionData` model that is implemented via pydantic.

### endpoint: json

The `json` endpoint returns canned json responses and headers.

### endpoint: match

The `match` endpoint compares the input data sent via `POST` or `PUT` against canned data. If canned headers are found for the tag in the URL, those will be compared as well.
A list of mismatches (or lack thereof) is returned as JSON.

### Testing

## Pytest
The [pytest](https://pypi.org/project/pytest/) tests in [test/pytest](test/pytest) can be executed using the pytest library.

If this app was properly installed, so was pytest!
Simply execute `pytest` in the project's directory (with the virtual environment activated) and the tests will be run.

## Karate
The [karate](https://karatelabs.github.io/karate/) tests in [test/karate](test/karate) can be executed using a karate executable.

**This repository does NOT contain a karate executable.**

If `wget` is installed, [get_karate.sh](get_karate.sh) can be used to download a version of the required jar file.

**A recent version of Java MUST be installed in order to run jar files like Karate.jar**

Once the `karate.jar` file is present in the project directory, Karate tests may be run using the official VS Code plugin, or by running [run_karate_tests.sh](run_karate_tests.sh)
