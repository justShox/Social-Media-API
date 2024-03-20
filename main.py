from fastapi import FastAPI
from users.user_api import user_router
from posts.post_api import post_router
from comments.comment_api import comment_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
