from pydantic import BaseModel, EmailStr
from models.events import Event
from typing import Optional, List
from beanie import Document, Link

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]
    class Settings:
        name = "users"
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }
    }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }
    }
