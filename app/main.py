from fastapi import FastAPI
from app.routers import car

app = FastAPI(title="Car API", description="A simple API for managing cars")

app.include_router(car.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Car API"} 