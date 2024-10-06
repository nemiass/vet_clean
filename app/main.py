from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.main import api_router
from app.models import *

from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api", tags=["API"])


@app.get("/", tags=["Root"])
def root():
    return {"message": "VET api"}
