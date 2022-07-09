from fastapi import FastAPI

import uvicorn
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Heroku test"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info")