# SpendWise Backend

A FastAPI based backend API for personal expense tracking with authentication.

## Features

- User signup and login
- JWT authentication
- Create expenses
- View user expenses
- Delete expenses
- SQLite database with SQLAlchemy ORM

## Tech Stack

- FastAPI
- Python
- SQLAlchemy
- JWT Authentication
- SQLite

## API Endpoints

POST /signup  
POST /login  
POST /expenses  
GET /expenses  
DELETE /expenses/{id}

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start server:

uvicorn app.main:app --reload

Open API docs:

http://127.0.0.1:8000/docs

## Example Request

Create expense:

POST /expenses

{
 "title": "coffee",
 "amount": 150
}

## Author

Harshita Vaghela