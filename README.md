# fastapi_sandbox

**Author:** Jeff Houle (jhoule86@gmail.com)

**Last Update:** June 2025

## Intro
A [fastapi](https://fastapi.tiangolo.com/) app for testing HTTP/REST clients.

## Setup

### Installation
1. Install python >= 3.13.3
2. Set up a virtual environment for Python using `venv`
2. Use [requirements.txt](requirements.txt) to install required dependencies, including the correct `fastapi` executable for the platform

### GET Responses
1. Make a copy of the [bin/response/sample](bin/response/sample) directory, with a meaningful name
2. Update the `payload.json` file to reflect the json payload to be returned
3. Update or remove the `headers.json` file to reflect the headers to be returned

## Running

Use the run script for your platform:
* Unix: [run.sh](run.sh)
* Windows: [run.cmd](run.cmd)
