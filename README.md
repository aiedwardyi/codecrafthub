# CodeCraftHub — Learning Management Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST_API-black?logo=flask)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-yellow?logo=javascript)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-blue?logo=css3)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight **learning management dashboard** built with **Flask and vanilla JavaScript**.
The application provides a simple **REST API backend** and a **single-page frontend dashboard** for managing learning courses.

The project focuses on **clean architecture, minimal dependencies, and clear API design**.

---

# Features

* Manage learning courses through a clean dashboard
* Full **CRUD REST API**
* Course progress tracking
* JSON file storage (no database required)
* Input validation for all course fields
* Course statistics endpoint
* Responsive single-page UI
* Real-time frontend → backend communication using `fetch()`

---

# Tech Stack

**Backend**

* Python
* Flask
* Flask-CORS

**Frontend**

* HTML5
* CSS3
* Vanilla JavaScript

**Storage**

* JSON (`courses.json`)

---

# Project Structure

```
codecrafthub/
│
├── app.py              # Flask REST API server
├── courses.json        # JSON storage for course data
├── index.html          # Single-page dashboard UI
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

# API Overview

Base URL

```
http://127.0.0.1:5050/api/courses
```

---

## Get All Courses

```
GET /api/courses
```

Returns a list of all courses.

---

## Get Course by ID

```
GET /api/courses/<id>
```

Returns details for a specific course.

---

## Create Course

```
POST /api/courses
```

Example request

```json
{
  "name": "Flask API Development",
  "description": "Learn to build REST APIs with Flask",
  "target_date": "2026-05-01",
  "status": "In Progress"
}
```

---

## Update Course

```
PUT /api/courses/<id>
```

Example request

```json
{
  "name": "Advanced Flask",
  "description": "Deep dive into Flask APIs",
  "target_date": "2026-06-01",
  "status": "Completed"
}
```

---

## Delete Course

```
DELETE /api/courses/<id>
```

Removes a course from storage.

---

## Course Statistics

```
GET /api/courses/stats
```

Example response

```json
{
  "total_courses": 4,
  "Not Started": 2,
  "In Progress": 1,
  "Completed": 1
}
```

---

# Running the Project

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Start the API server

```
python app.py
```

The API will start at

```
http://127.0.0.1:5050
```

### 3. Open the dashboard

Open the frontend file in your browser:

```
index.html
```

The dashboard will automatically connect to the running API.

---

# Application Architecture

The project follows a simple **API-first architecture**.

```
Frontend (index.html)
      │
      │  HTTP requests (fetch API)
      ▼
Flask REST API (app.py)
      │
      ▼
JSON Storage (courses.json)
```

* The **frontend** handles UI rendering and user interaction.
* The **Flask API** processes requests and performs validation.
* Course data is stored in a lightweight **JSON file**.

This design keeps the project simple while demonstrating **full-stack interaction between a frontend interface and backend API**.

---

# Example API Test

Example request using PowerShell:

```
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:5050/api/courses"
```

---

# License

This project is licensed under the **MIT License**.

See the full license here:

[LICENSE](LICENSE)

---

# Author

**Edward Yi**

Software developer focused on building practical systems combining **software engineering, APIs, and AI-driven applications**.
