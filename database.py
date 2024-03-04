from tortoise.contrib.fastapi import register_tortoise

def register_tortoise(app):
    register_tortoise(
        app,
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']},
        generate_schemas=True,
        add_exception_handlers=True
    )
