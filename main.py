from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import models
from db.database import engine
from router import blog_get, blog_post, user, article, product
from auth import authentication


app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


models.Base.metadata.create_all(engine)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
