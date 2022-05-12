from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from . routers import post, user, auth, votes
from .config import Settings

# run command
# uvicorn main:app --reload

# models.Base.metadata.create_all(bind=engine) / using alembic now


origins = ["*"]

app = FastAPI()
# middleware - function runs first before every request
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

            
# request get method url:/
@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}














    