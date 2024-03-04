from pydantic import BaseModel

class UserIn(BaseModel):
    username: str

class PostIn(BaseModel):
    title: str
    content: str
    author_id: int
    category: str
