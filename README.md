# Deployment Example

This is a *very* basic example project to use for toy deployment.

## Installation

`pip3 install -r requirements.txt`

## Environment

This app requires a root-level `.env` file with the following keys:

```sh
PORT=XXXX
HOST=X.X.X.X
DEBUG=0
```

Replace all `X` with relevant values.

## Development

`python3 main.py`

## API usage

When running, this project provides a simple JSON API that answers yes/no questions.

| Route | Method | Function |
| --- | --- | --- |
| `/` | `GET` | Describes the API |
| `/decide` | `GET` | Answers a yes/no question using AI |
