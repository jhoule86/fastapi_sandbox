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

You may craft custom responses for the `/json` endpoint:
1. Make a copy of the [bin/response/sample](bin/response/sample) directory, with a meaningful name
2. Update the `payload.json` file to reflect the json payload to be returned
3. Update or remove the `headers.json` file to reflect the headers to be returned

## Running

Use the run script for your platform:
* Unix: [run.sh](run.sh)
* Windows: [run.cmd](run.cmd)

## Usage

**The included [http_requests/sample.http](http_requests/sample.http) file contains example requests for execution via clients such as the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension for VS Code.**

### endpoint: get

The `get` endpoint returns a simple json response based on a small `TransactionData` model that is implemented via pydantic.

### endpoint: post

The `post` endpoint echoes a simple json request that is expected to match the schema of the `TransactionData` model that is implemented via pydantic.

### endpoint: json

The `json` endpoint returns canned json responses and headers.

### endpoint: match

The `match` endpoint compares the POSTed data (and optionally headers) against canned data.
A list of mismatches (or lack thereof) is returned as JSON.

