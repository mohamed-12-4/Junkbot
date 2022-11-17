from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

#from .routers import post, user, auth, vote

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]


@app.get('/')
async def main():
    return {"Test": "Test"}

@app.get('/database')
async def database(db: Session = Depends(get_db())):
    return {"S": "Yay"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
"""