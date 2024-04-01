from urllib.parse import urlparse
from fastapi import Body, FastAPI, Header
import os
from fastapi.responses import JSONResponse
import requests

app = FastAPI()
ollama_url = os.getenv('OLLAMA_URL')
print("Proxy to: " + ollama_url)
base_hostname = urlparse(ollama_url).netloc

def response_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

@app.post('/api/generate')
async def proxy(authorization: str = Header(None), data: dict = Body(...)):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization,
        'host': base_hostname
    }
    rez = requests.post(ollama_url + '/api/generate', json=data, headers=headers)
    response = JSONResponse(content=rez.json())
    response_headers(response)
    return response

@app.options('/api/generate')
async def options_handler():
    response = JSONResponse(content={'message': 'CORS headers allowed.'})
    response_headers(response)
    return response

if __name__ == '__main__':
    import uvicorn
    port = int(os.getenv('PORT', 80))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")