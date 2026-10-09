
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "students.db"


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                course TEXT NOT NULL
            )
        """)


@app.route("/")
def home():
    return jsonify({"message": "Student Management API is running"})


# CREATE
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    if not all(isinstance(v, str) and v.strip()
               for v in (name, email, course)):
        return jsonify({
            "error": "name, email and course are required"
        }), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.execute(
                "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                (name.strip(), email.strip(), course.strip())
            )
            student_id = cursor.lastrowid

        return jsonify({
            "id": student_id,
            "name": name.strip(),
            "email": email.strip(),
            "course": course.strip()
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409


# READ ALL
@app.route("/students", methods=["GET"])
def get_students():
    with sqlite3.connect(DATABASE) as conn:
        rows = conn.execute(
            "SELECT id, name, email, course FROM students"
        ).fetchall()

    students = [
        {"id": r[0], "name": r[1], "email": r[2], "course": r[3]}
        for r in rows
    ]
    return jsonify(students), 200


# READ ONE
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    with sqlite3.connect(DATABASE) as conn:
        row = conn.execute(
            "SELECT id, name, email, course FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()

    if row is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "id": row[0], "name": row[1],
        "email": row[2], "course": row[3]
    }), 200


# UPDATE
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    if not all(isinstance(v, str) and v.strip()
               for v in (name, email, course)):
        return jsonify({
            "error": "name, email and course are required"
        }), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.execute("""
                UPDATE students SET name=?, email=?, course=?
                WHERE id=?
            """, (name.strip(), email.strip(), course.strip(), student_id))

            if cursor.rowcount == 0:
                return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student updated successfully"}), 200

    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409


# DELETE
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "DELETE FROM students WHERE id=?", (student_id,)
        )

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)