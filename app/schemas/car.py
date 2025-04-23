from pydantic import BaseModel

class Car(BaseModel):
    id: int
    name: str
    brand: str
    year: int
    price: float 