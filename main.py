
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from routes import users, posts
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        }
    },
}

Tortoise.init(config=TORTOISE_ORM)

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(users.router)
app.include_router(posts.router)



if __name__ == "__main__":
    run_async(app)
