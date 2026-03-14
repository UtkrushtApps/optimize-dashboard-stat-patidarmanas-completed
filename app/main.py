from fastapi import FastAPI
from app.routes import api

app = FastAPI(title="Shopboard Dashboard API")
app.include_router(api.router)
