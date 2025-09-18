from fastapi import FastAPI
from . import  models
from .database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get("/health")
def health():
  return {"status": "ok"}