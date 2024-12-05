from fastapi import FastAPI
from . import models, schemas
from .database import engine
from .routers import post, user, auth, votes
from fastapi.middleware.cors import CORSMiddleware




# models.Base.metadata.create_all(bind=engine)
# schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8000",  # Permitir localhost
    "http://localhost",       # Para outras portas
    "http://127.0.0.1",       # Para IPv4
]
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




@app.get("/")
async def root():
    return {"message": "Welcome to my API"}



