from fastapi import FastAPI
from app.api.v1.routes.health import router

app = FastAPI()
app.include_router(router)
