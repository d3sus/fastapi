from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from database.connection import Settings
from models.users import User
from models.events import Event
from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI()
settings = Settings()
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[User, Event]
    )
    print("Database initialized!")
    yield
    # Здесь можно закрыть соединение, если нужно
    client.close()
    print("App shutdown!")
    
@app.get("/")
async def home():
    return "hello"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
