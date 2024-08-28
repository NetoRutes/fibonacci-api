# Fibonacci Project

## Overview

This API generates the first n Fibonacci numbers, caching results in a relational database to avoid redundant calculations.

## Features
- Generates Fibonacci sequences based on user input.
- Stores calculated sequences in the database for efficiency.
- Provides a user-friendly API with clear error handling.
- Includes unit tests for ensuring API functionality.
- Offers interactive API documentation using Swagger.

## Installation

### Main Prerequisites

- Coverage
- Django
- Django REST Framework
- Python 3.x
- SQLite
- Pytest
- Pytest-django

### Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/NetoRutes/fibonacci-api.git
    ```

2. **Create and activate a virtual env:**
    ```bash
    python -m venv env && source env/bin/activate
    ```

3. **Install the required software packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations**
    ```bash
    python manage.py migrate
    ```

## Usage
1. Run the development server: 
    ```bash
    python manage.py runserver
    ```
2. Access the API documentation at: **http://localhost:8000/swagger/**
3. Send a POST request to `/api/v1/generate/` with the following JSON data:
    ```json
    {
        "n_value": 10  // Replace with your desired sequence length
    }
    ```
4. The response will contain the calculated Fibonacci sequence for n_value or an error message if the request is invalid.

## Testing
### To run the unit tests:
    python manage.py test fibonacci

## Additional Notes:

- The `models.py` file defines a FibonacciNumber model to store calculated sequences in the database.
- The `serializers.py` file provides a serializer for the FibonacciNumber model for API interactions.
- The `views.py` file implements the API endpoint for generating Fibonacci sequences.
- The `tests.py` file contains unit tests to ensure the functionality of the API.
- The `swagger.py` file configures Swagger for interactive API documentation.

## Future Enhancements

- Utilize better cache storage tool like Redis.
- To allow background processing tasks for large n Fibonacci sequences utilize a queue system with tool like Celery. Than the frontend should poll the backend at regular intervals to check if the sequence has been generated.