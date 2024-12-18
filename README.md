# Wildlife Sightings API
This FastAPI-based project is a RESTful API designed to manage wildlife sightings. The API supports common CRUD operations: creating, reading, updating, and deleting wildlife sightings, with filtering options based on species and location. The sighting data is stored in an in-memory database (Python dictionary), which can be extended later for persistent storage solutions like SQL or NoSQL databases.

# Features:
Create a Sighting: Add a new wildlife sighting by providing species, location, date, and time. The species and location names are automatically validated to be capitalized, and the date and time must follow the format YYYY-MM-DD and HH:MM respectively.

Retrieve Sightings:

Fetch all sightings.
Filter sightings by species or location.
Retrieve by ID: Fetch details of a specific sighting by providing its unique ID.

Update a Sighting: Modify an existing sighting's details, such as species, location, date, and time.

Delete a Sighting: Remove a sighting by ID.
# Future Enhancements
v1: Wildlife tracking using FastAPI and a dictionary for data storage.

v2: Wildlife tracking using FastAPI and PostgreSQL for data storage.

v3: Wildlife tracking using FastAPI for the backend, PostgreSQL for the database, and Streamlit for the frontend.
# Endpoints:
POST /sightings: Create a new sighting.

GET /sightings: Get a list of all sightings (optionally filter by species and location).

GET /sightings/{id}: Get details of a sighting by ID.

PUT /sightings/{id}: Update an existing sighting.

DELETE /sightings/{id}: Delete a sighting by ID.
Validation:
Species & Location: Must be capitalized and within specified character limits.
Date & Time: Validates input formats to ensure correctness.

# view
Once the application is running, visit http://localhost:8000/docs for interactive API documentation using Swagger UI.
# License
This project is licensed under the [RIVON-AI](https://github.com/rivon-ai) License. See the LICENSE file for details.
