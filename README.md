# TripView API

TripView is a university project developed to work with Kotlin and help users share their experiences in traveling. This repository contains the API written in Python to support the TripView application.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributors](#contributors)
- [License](#license)

## Introduction
TripView API is designed to provide backend support for the TripView application, allowing users to share and view travel experiences. 

## Installation
To install and run the TripView API, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/tesinitsyn/trip-view.git
    ```

2. Navigate to the API directory:
    ```sh
    cd TripView/api
    ```

3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Run the API server:
    ```sh
    python app.py(or not idk)
    ```

## Usage
To use the TripView API, send HTTP requests to the endpoints defined below. You can use tools like `curl`, Postman, or any HTTP client to interact with the API.

## API Endpoints
Here are some example endpoints that the TripView API might expose:

- `GET /trips` - Retrieve a list of all trips
- `POST /trips` - Create a new trip
- `GET /trips/{id}` - Retrieve a specific trip by ID
- `PUT /trips/{id}` - Update a specific trip by ID
- `DELETE /trips/{id}` - Delete a specific trip by ID

### Example Request
```sh
curl -X GET http://localhost:5000/trips
```

## Contributors
This project is maintained by the following contributor:
- [tesinitsyn](https://github.com/tesinitsyn)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
