
import uvicorn
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI(
    title='FastAPI JWT', openapi_url='/openapi.json', docs_url='/docs',
    description='fastapi jwt')


if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=5000, log_level="info")
