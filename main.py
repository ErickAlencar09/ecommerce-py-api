from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

@app.get("/")
def index():
    return {"Message": "Hello world"}

register_tortoise(
    app,
    db_url="mysql://root:admin@localhost:3306/ecommercepy",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)