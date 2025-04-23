# fastapi-crud-carapi

A simple FastAPI-based REST API for managing car inventory. This project demonstrates a modular FastAPI application structure with basic CRUD operations.

## Project Structure

```
app/
├── __init__.py
├── main.py
├── models/
│   └── __init__.py
├── routers/
│   ├── __init__.py
│   └── car.py
└── schemas/
    ├── __init__.py
    └── car.py
```

## Features

- Create, Read, Update, and Delete (CRUD) operations for cars
- RESTful API endpoints
- Pydantic models for data validation
- Modular project structure

## API Endpoints

- `GET /` - Welcome message
- `GET /cars` - Get all cars
- `POST /cars` - Add a new car
- `PUT /cars/{id}` - Update a car
- `DELETE /cars/{id}` - Delete a car

## Car Model

```json
{
    "id": 1,
    "name": "Model S",
    "brand": "Tesla",
    "year": 2025,
    "price": 79990.00
}
```

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Dependencies

The project uses the following main packages:

- `fastapi==0.115.12` - A modern, fast web framework for building APIs
- `uvicorn==0.34.2` - ASGI server implementation for running FastAPI applications
- `pydantic==2.11.3` - Data validation and settings management using Python type annotations
- `starlette==0.46.2` - Lightweight ASGI framework/toolkit (dependency of FastAPI)

Additional dependencies include:
- `annotated-types` - Runtime support for type annotations
- `anyio` - High level asynchronous I/O
- `click` - Command line interface creation kit
- `colorama` - Cross-platform colored terminal text
- `h11` - Pure-Python HTTP/1.1 client library
- `idna` - Internationalized Domain Names in Applications
- `pydantic_core` - Core validation logic for Pydantic
- `sniffio` - Sniff out which async library your code is running under
- `typing-inspection` - Runtime inspection utilities for typing
- `typing_extensions` - Backported and experimental type hints

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application using uvicorn, use the following command:

```bash
uvicorn app.main:app --reload
```

The `--reload` flag enables auto-reload when code changes are detected.

Once running, you can access:
- The API at: `http://localhost:8000`
- The interactive API documentation at: `http://localhost:8000/docs`
- The alternative API documentation at: `http://localhost:8000/redoc`

## Example API Usage

1. Add a new car:
```bash
curl -X POST "http://localhost:8000/cars" \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "name": "Model S", "brand": "Tesla", "year": 2023, "price": 79990.00}'
```

2. Get all cars:
```bash
curl "http://localhost:8000/cars"
```

3. Update a car:
```bash
curl -X PUT "http://localhost:8000/cars/1" \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "name": "Model S", "brand": "Tesla", "year": 2023, "price": 84990.00}'
```

4. Delete a car:
```bash
curl -X DELETE "http://localhost:8000/cars/1"
```

## Development

This project uses a modular structure:
- `app/schemas/` - Contains Pydantic models for data validation
- `app/routers/` - Contains route handlers for different API endpoints
- `app/models/` - Reserved for database models (when implemented)
- `app/main.py` - Main application file that ties everything together

## License

This project is open source and available under the MIT License. 