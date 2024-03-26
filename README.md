# AI API Proxy

A basic proxy for ``ollama`` api that forward the requests from localhost to a remote.

## Installing

```bash
# make virtual environment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Set Up

```bash
cp .env.example .env

# edit environment
vim .env 
```

## Running 

### Local

```bash
python proxy.py
```

### Apache2

```httpd
<VirtualHost *:80>
    ServerName myaiproxy.com
    DocumentRoot /path/to/ai-api-proxy/

    WSGIDaemonProcess myflaskapp user=www-data group=www-data threads=5
    WSGIProcessGroup myflaskapp
    WSGIScriptAlias / /path/to/ai-api-proxy/proxy.py
</VirtualHost>
```