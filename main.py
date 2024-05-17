from fastapi import FastAPI
from os import getenv
import uvicorn

app = FastAPI()
    
if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("app.api:app", port=port, reload=True)