# Todo List API

## Description

This API allows you to manage a to-do list. It is developed using Flask and Flask-RESTX, providing CRUD (Create, Read, Update, Delete) functionalities to manage tasks.

### Features:
- Create a new task
- Get the list of all tasks
- Retrieve a specific task by ID
- Update an existing task
- Delete a task

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://127.0.0.1:5000/`.

## Swagger Documentation

The API is documented with Swagger, automatically generated using Flask-RESTX. You can access the Swagger documentation by visiting:

```
http://127.0.0.1:5000/
```

## Endpoints

### `GET /tasks/`
- **Description**: Retrieve all tasks.
- **Response**:
  - `200 OK`: Successfully retrieved the list of tasks.

### `POST /tasks/`
- **Description**: Add a new task.
- **Request Body**:
  ```json
  {
    "title": "Buy milk",
    "done": false
  }
  ```
- **Response**:
  - `201 Created`: Task successfully added.
  - `400 Bad Request`: Invalid data.

### `GET /tasks/<int:id>`
- **Description**: Retrieve a specific task by ID.
- **Response**:
  - `200 OK`: Successfully retrieved the task.
  - `404 Not Found`: Task not found.

### `PUT /tasks/<int:id>`
- **Description**: Update an existing task by ID.
- **Request Body**:
  ```json
  {
    "title": "Buy bread",
    "done": true
  }
  ```
- **Response**:
  - `200 OK`: Task successfully updated.
  - `404 Not Found`: Task not found.

### `DELETE /tasks/<int:id>`
- **Description**: Delete a task by ID.
- **Response**:
  - `200 OK`: Task successfully deleted.
  - `404 Not Found`: Task not found.

## Data Model

The task data model is defined as follows:
- `id`: Unique identifier for the task (integer).
- `title`: Title of the task (string).
- `done`: Status of the task (boolean).

## Technologies Used
- **Flask**: Web framework for Python.
- **Flask-RESTX**: Extension for Flask to create REST APIs and generate Swagger documentation.
- **SQLAlchemy**: ORM for managing the SQLite database.

## Running Tests

To run unit tests (if available):
```bash
pytest
```

## Contribution

Contributions are welcome. If you want to add features or fix bugs, please create a pull request on the repository.

## License

This project is licensed under the MIT License. Please see the `LICENSE` file for more information.

