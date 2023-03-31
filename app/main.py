from fastapi import FastAPI
from app.api.image import router as image_router

app = FastAPI()

app.include_router(image_router, prefix="/api")

