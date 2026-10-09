# API Documentation

## Base URL

`http://127.0.0.1:5000`

## 1. Create Student

**Method:** POST

**Endpoint:** `/students`

**Request Body:**

```json
{
  "name": "Saanvi",
  "email": "saanvi@example.com",
  "course": "Computer Science"
}
```

**Success:** `201 Created`

## 2. Retrieve All Students

**Method:** GET

**Endpoint:** `/students`

**Success:** `200 OK`

Returns a JSON array of student records.

## 3. Retrieve One Student

**Method:** GET

**Endpoint:** `/students/{id}`

**Success:** `200 OK`

**Error:** `404 Not Found`

## 4. Update Student

**Method:** PUT

**Endpoint:** `/students/{id}`

Send all three required fields: `name`, `email`, and `course`.

**Success:** `200 OK`

**Errors:** `400 Bad Request`, `404 Not Found`, `409 Conflict`

## 5. Delete Student

**Method:** DELETE

**Endpoint:** `/students/{id}`

**Success:** `200 OK`

**Error:** `404 Not Found`

## Error Status Codes

| Code | Meaning                    |
| ---- | -------------------------- |
| 400  | Invalid or missing input   |
| 404  | Student or route not found |
| 405  | HTTP method not allowed    |
| 409  | Duplicate email address    |
| 415  | Unsupported content type   |

All responses are returned in JSON format.
