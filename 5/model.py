from pydantic import BaseModel
from typing import List

class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "item": "Example schema!"
            }
        }
    }

class TodoItems(BaseModel):

    todos: List[TodoItem]

    model_config = {
        "json_schema_extra": {
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"}
                ]
            }
        }
    }

class Todo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }
    }

