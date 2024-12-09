from fastapi import FastAPI, Depends
from . import models, schemas
from .database import engine
from .routers import post, user, auth, votes
from fastapi.middleware.cors import CORSMiddleware




# models.Base.metadata.create_all(bind=engine)
# schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8000",  
    "http://localhost",      
    "http://127.0.0.1",       
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
    return {"message": " hello, I am pushing out to ubuntu "}

# @app.post("/users/", response_model=schemas.UserOut, status_code=201)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = models.User(email=user.email, password=user.password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

