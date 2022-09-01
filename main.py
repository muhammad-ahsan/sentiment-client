import uuid

import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/get_server_response")
async def get_server_response(parameter: str):
    api_url = "http://sentiment-server:8000/predict?q=" + parameter
    try:
        response = requests.get(api_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the backend server')
        raise SystemExit(e)


@app.get("/health")
async def health():
    return {"message": "Congratulations, sentiment client is healthy :) "}


@app.get("/")
async def root():
    return {"message": "I am the sentiment client"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
