
# Unicornify API 🦄

A random app with multiple services

## Requirements

* Python 3.10+
* pipenv

## Getting started

Create a `.env` file in this directory and insert the key-value pairs in the following format of `KEY=VALUE`

```sh
BACKEND_CORS_ORIGINS=['http://localhost', 'http://localhost:5173', 'https://localhost', 'http://127.0.0.1:5173']
PROJECT_NAME = Unicornify
```

Install dependencies and run development server

```bash
# make sure you have pipenv installed then install dependencies
$ pipenv install

# get into the virtual environment
$ pipenv shell

# run the live server
$ uvicorn app.main:app --reload
```

## Running tests

```bash
# to start running tests, run this command in virtualenv:
$ pytest -v
```
