from fastapi import FastAPI
from app.api.v1.endpoints import recipes

app = FastAPI(title="FastAPI Recipe App")

app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Recipe App"}
