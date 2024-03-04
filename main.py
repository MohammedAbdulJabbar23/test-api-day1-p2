from fastapi import FastAPI
from routes import users, posts
from database import register_tortoise
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


register_tortoise(
        app,
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']},
        generate_schemas=True,
        add_exception_handlers=True
    )


app.include_router(users.router)
app.include_router(posts.router)

