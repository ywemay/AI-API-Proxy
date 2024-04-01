# AI API Proxy

A basic proxy for ``ollama`` api that forwards the requests from localhost to a remote.

## Set Up

```bash
cp .env.example .env

# edit environment
vim .env 
```

## Docker

```bash

docker compose up -d --build
```

## On local machine

```bash
# make virtual environment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# run
. .env && python proxy.py
```
