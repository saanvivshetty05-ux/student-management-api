# Student Management REST API

## Project Overview

This project is a RESTful API developed using Python, Flask, and SQLite. It allows users to create, retrieve, update, and delete student records.

## Technologies Used

* Python
* Flask
* SQLite
* JSON
* Requests (for API testing)

## Features

* Create student records
* Retrieve all students
* Retrieve a student by ID
* Update student details
* Delete student records
* Input validation
* Error handling
* JSON responses
* Database integration

## Installation and Setup

1. Clone or download this repository.

2. Open the project folder in VS Code.

3. Create a virtual environment:

   `python -m venv venv`

4. Activate the environment in PowerShell:

   `.\venv\Scripts\Activate.ps1`

5. Install dependencies:

   `python -m pip install -r requirements.txt`

6. Start the API:

   `python app.py`

7. Open `http://127.0.0.1:5000/` in a browser.

## API Endpoints

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| POST   | `/students`      | Create a student       |
| GET    | `/students`      | Retrieve all students  |
| GET    | `/students/{id}` | Retrieve one student   |
| PUT    | `/students/{id}` | Update student details |
| DELETE | `/students/{id}` | Delete a student       |

## Student Data Model

* `id`: Integer, automatically generated primary key
* `name`: String, required
* `email`: String, required and unique
* `course`: String, required

## Error Handling

The API returns JSON error messages for invalid input, missing students, duplicate email addresses, and unsupported routes or HTTP methods.

## Database

SQLite stores student records in `students.db`. The database table is created automatically when the application starts.

## API Documentation

See `API_DOCUMENTATION.md` for endpoint details, request examples, and response codes.
