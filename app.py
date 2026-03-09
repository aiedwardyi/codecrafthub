from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS so a frontend can call this API

DATA_FILE = "courses.json"
VALID_STATUSES = ["Not Started", "In Progress", "Completed"]


# Create courses.json automatically if it does not exist
def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump([], file)
        except IOError:
            print("Error: Could not create courses.json")


# Read all courses from the JSON file
def load_courses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        initialize_data_file()
        return []
    except json.JSONDecodeError:
        return []
    except IOError:
        raise Exception("Error reading courses file")


# Save all courses to the JSON file
def save_courses(courses):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(courses, file, indent=4)
    except IOError:
        raise Exception("Error writing to courses file")


# Generate the next course ID automatically
def get_next_id(courses):
    if not courses:
        return 1
    return max(course["id"] for course in courses) + 1


# Validate course input data
def validate_course_data(data):
    required_fields = ["name", "description", "target_date", "status"]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return f"Missing or empty required field: {field}"

    if data["status"] not in VALID_STATUSES:
        return f"Invalid status. Must be one of: {', '.join(VALID_STATUSES)}"

    try:
        datetime.strptime(data["target_date"], "%Y-%m-%d")
    except ValueError:
        return "Invalid target_date format. Use YYYY-MM-DD"

    return None


# Home route for quick testing
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to CodeCraftHub API",
        "status": "API is running"
    }), 200


# GET all courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    try:
        courses = load_courses()
        return jsonify(courses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET a specific course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    try:
        courses = load_courses()
        course = next((course for course in courses if course["id"] == course_id), None)

        if not course:
            return jsonify({"error": "Course not found"}), 404

        return jsonify(course), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# POST create a new course
@app.route("/api/courses", methods=["POST"])
def add_course():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body must be valid JSON"}), 400

        validation_error = validate_course_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        courses = load_courses()

        new_course = {
            "id": get_next_id(courses),
            "name": data["name"].strip(),
            "description": data["description"].strip(),
            "target_date": data["target_date"],
            "status": data["status"],
            "created_at": datetime.now().isoformat()
        }

        courses.append(new_course)
        save_courses(courses)

        return jsonify({
            "message": "Course created successfully",
            "course": new_course
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# PUT update an existing course
@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body must be valid JSON"}), 400

        validation_error = validate_course_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        courses = load_courses()
        course = next((course for course in courses if course["id"] == course_id), None)

        if not course:
            return jsonify({"error": "Course not found"}), 404

        course["name"] = data["name"].strip()
        course["description"] = data["description"].strip()
        course["target_date"] = data["target_date"]
        course["status"] = data["status"]

        save_courses(courses)

        return jsonify({
            "message": "Course updated successfully",
            "course": course
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# DELETE a course
@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    try:
        courses = load_courses()
        course = next((course for course in courses if course["id"] == course_id), None)

        if not course:
            return jsonify({"error": "Course not found"}), 404

        courses = [course for course in courses if course["id"] != course_id]
        save_courses(courses)

        return jsonify({"message": "Course deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/api/courses/stats", methods=["GET"])
def get_course_stats():
    try:
        courses = load_courses()

        stats = {
            "total_courses": len(courses),
            "Not Started": 0,
            "In Progress": 0,
            "Completed": 0
        }

        for course in courses:
            status = course.get("status")
            if status in stats:
                stats[status] += 1

        return jsonify(stats), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    initialize_data_file()
    app.run(debug=True, port=5050)