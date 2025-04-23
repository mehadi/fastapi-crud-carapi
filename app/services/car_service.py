from typing import List
from app.schemas.car import Car

class CarService:
    def __init__(self):
        self.cars: List[Car] = []

    def get_all_cars(self) -> List[Car]:
        return self.cars

    def get_car_by_id(self, car_id: int) -> Car:
        for car in self.cars:
            if car.id == car_id:
                return car
        return None

    def add_car(self, car: Car) -> Car:
        # Check if car with same ID exists
        if self.get_car_by_id(car.id):
            raise ValueError(f"Car with ID {car.id} already exists")
        self.cars.append(car)
        return car

    def update_car(self, car_id: int, updated_car: Car) -> Car:
        for i in range(len(self.cars)):
            if self.cars[i].id == car_id:
                self.cars[i] = updated_car
                return updated_car
        return None

    def delete_car(self, car_id: int) -> bool:
        for i in range(len(self.cars)):
            if self.cars[i].id == car_id:
                del self.cars[i]
                return True
        return False

# Create a singleton instance
car_service = CarService() 