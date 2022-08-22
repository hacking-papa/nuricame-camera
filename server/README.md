# nuricame-camera - Server

Make a contour by pictures, version with separated camera.

- [Prerequisites](#prerequisites)
- [How to](#how-to)
  - [Setup](#setup)
  - [Launch](#launch)
  - [Test](#test)
    - [Using httpie](#using-httpie)
- [Misc](#misc)
  - [License](#license)

## Prerequisites

- Python 3
  - FastAPI

## How to

### Setup

`python3 -m venv venv` to create virtual environment.

`source venv/bin/activate` to activate the virtual environment.

`pip install --upgrade pip && pip install -r requirements.txt` to install dependencies.

### Launch

`uvicorn --host 0.0.0.0 --port 8000 --reload main:app` to launch the server.

Then `http://0.0.0.0:8000/` is the end point.

To see API document, access to `http://0.0.0.0:8000/docs` or `http://0.0.0.0:8000/redoc`.

### Test

#### Using [httpie](https://httpie.io)

`http --form POST http://0.0.0.0:8000/ file@samples/Airplane.jpg`

## Misc

### License

The software is distributed freely under **GOOD DADDY LICENSE**, see [LICENSE](LICENSE).
