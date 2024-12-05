from contextlib import asynccontextmanager

from fastapi import FastAPI, Body
import uvicorn
from views.profile.registration import router as registration_profile_router

@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(registration_profile_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hyi copchenie"
    }


@app.get("/hello/")
def hello(name: str = Body()):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
