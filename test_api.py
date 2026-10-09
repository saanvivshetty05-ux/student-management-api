
import requests

BASE_URL = "http://127.0.0.1:5000"

# 1. CREATE a student
student = {
    "name": "Saanvi",
    "email": "saanvi@example.com",
    "course": "Computer Science"
}

response = requests.post(
    f"{BASE_URL}/students",
    json=student
)
print("CREATE:", response.status_code, response.text)

# 2. READ all students
response = requests.get(f"{BASE_URL}/students")
print("READ:", response.status_code, response.text)

# 3. UPDATE the created student
if response.status_code == 200:
    students = response.json()

    if students:
        student_id = students[-1]["id"]

        updated = {
            "name": "Saanvi",
            "email": "saanvi@example.com",
            "course": "Data Science"
        }

        response = requests.put(
            f"{BASE_URL}/students/{student_id}",
            json=updated
        )
        print("UPDATE:", response.status_code, response.text)

        # 4. DELETE the student
        response = requests.delete(
            f"{BASE_URL}/students/{student_id}"
        )
        print("DELETE:", response.status_code, response.text)