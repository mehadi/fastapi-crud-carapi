from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.car import Car

router = APIRouter(prefix="/cars", tags=["cars"])

cars: List[Car] = []

@router.get("/")
def get_cars():
    return cars

@router.post("/")
def add_car(car: Car):
    # Check if car with same ID exists
    for existing_car in cars:
        if existing_car.id == car.id:
            raise HTTPException(
                status_code=400,
                detail=f"Car with ID {car.id} already exists"
            )
    cars.append(car)
    return car

@router.put("/{id}")
def update_car(id: int, updated_car: Car):
    for i in range(len(cars)):
        if cars[i].id == id:
            cars[i] = updated_car
            return updated_car
    return {"error": "Car not found!"}

@router.delete("/{id}")
def delete_car(id: int):
    for i in range(len(cars)):
        if cars[i].id == id:
            del cars[i]
            return {"message": "Car deleted successfully!"}
    return {"error": "Car not found!"} 