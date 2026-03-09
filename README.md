# CodeCraftHub

## Project Overview

CodeCraftHub is a simple REST API built with **Python and Flask** that
allows developers to track programming courses they want to learn.

The project demonstrates the basics of building a **CRUD (Create, Read,
Update, Delete) REST API** without using a database. Instead, course
data is stored in a simple **JSON file**.

---------------

## Features

- Create new learning courses
- View all courses
- View a specific course
- Update existing courses
- Delete courses
- JSON file storage (no database required)
- Input validation for required fields
- Status validation (`Not Started`, `In Progress`, `Completed`)
- Auto-generated course IDs
- Timestamp tracking (`created_at`)
- CORS enabled for frontend integration

------------------------------------------------------------------------

## Project Structure

    codecrafthub/
    │
    ├── app.py # Main Flask REST API application
    ├── courses.json # JSON file used as simple storage
    ├── requirements.txt # Python dependencies
    ├── README.md # Project documentation
    └── LICENSE # MIT License for open-source us

------------------------------------------------------------------------

## Installation Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/aiedwardyi/codecrafthub.git
cd codecrafthub
```

### 2. Create a virtual environment (recommended)

``` bash
python -m venv venv
```

Activate the environment:

**Windows**

``` bash
venv\Scripts\activate
```

**Mac/Linux**

``` bash
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Running the Application

Start the Flask server:

``` bash
python app.py
```

The API will run at:

    http://127.0.0.1:5050

If `courses.json` does not exist, it will automatically be created when
the server starts.

------------------------------------------------------------------------

## API Endpoints

Base URL:

    http://127.0.0.1:5050

### Create a Course

**POST** `/api/courses`

Example:

``` bash
curl -X POST http://127.0.0.1:5050/api/courses -H "Content-Type: application/json" -d "{"name":"Python Basics","description":"Learn Python fundamentals","target_date":"2026-04-15","status":"Not Started"}"
```

------------------------------------------------------------------------

### Get All Courses

**GET** `/api/courses`

``` bash
curl http://127.0.0.1:5050/api/courses
```

------------------------------------------------------------------------

### Get a Single Course

**GET** `/api/courses/{id}`

``` bash
curl http://127.0.0.1:5050/api/courses/1
```

------------------------------------------------------------------------

### Update a Course

**PUT** `/api/courses/{id}`

``` bash
curl -X PUT http://127.0.0.1:5050/api/courses/1 -H "Content-Type: application/json" -d "{"name":"Python Basics Updated","description":"Updated description","target_date":"2026-05-01","status":"In Progress"}"
```

------------------------------------------------------------------------

### Delete a Course

**DELETE** `/api/courses/{id}`

``` bash
curl -X DELETE http://127.0.0.1:5050/api/courses/1
```

------------------------------------------------------------------------

### Get Course Statistics

**GET** `/api/courses/stats`

Returns statistics about the stored courses.

``` bash
curl http://127.0.0.1:5050/api/courses/stats
```

Example response:

{
  "total_courses": 3,
  "Not Started": 1,
  "In Progress": 1,
  "Completed": 1
}

------------------------------------------------------------------------

## Testing the API

You can test the API using:

- `curl`
- PowerShell `Invoke-RestMethod`
- Postman
- Thunder Client (VS Code extension)

Example PowerShell test:

``` powershell
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:5050/api/courses"
```

------------------------------------------------------------------------

## Troubleshooting

### Port already in use

If port `5050` is busy, modify the port in `app.py`:

``` python
app.run(debug=True, port=5051)
```

### Module not found error

Make sure dependencies are installed:

``` bash
pip install -r requirements.txt
```

### courses.json not found

The application automatically creates `courses.json` if it does not
exist.

------------------------------------------------------------------------

## Learning Objectives

This project demonstrates:

- REST API design
- CRUD operations
- Flask backend development
- JSON file storage
- Input validation
- API testing with curl
- CORS configuration

------------------------------------------------------------------------

## License

This project is licensed under the [MIT License](LICENSE).
