from fastapi import APIRouter, HTTPException
from app.schemas.car import Car
from app.services.car_service import car_service

router = APIRouter(prefix="/cars", tags=["cars"])

@router.get("/")
def get_cars():
    return car_service.get_all_cars()

@router.post("/")
def add_car(car: Car):
    try:
        return car_service.add_car(car)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{id}")
def update_car(id: int, updated_car: Car):
    result = car_service.update_car(id, updated_car)
    if result is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return result

@router.delete("/{id}")
def delete_car(id: int):
    if not car_service.delete_car(id):
        raise HTTPException(status_code=404, detail="Car not found")
    return {"message": "Car deleted successfully!"} 