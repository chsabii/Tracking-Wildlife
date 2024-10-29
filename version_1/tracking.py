from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Dict, List, Optional

app = FastAPI()

# In-memory database to store sightings
sightings_db: Dict[int, dict] = {}

# Define the Sighting model
class Sighting(BaseModel):
    id: int = Field(example="Enter ID")
    species: str = Field(..., min_length=3, max_length=50, example="Enter Species Name")
    location: str = Field(..., min_length=3, max_length=100, example="Enter Species Location")
    date: str = Field(..., description="Date in 'YYYY-MM-DD' format", example="2024-10-16")
    time: str = Field(..., description="Time in 'HH:MM' format", example="14:30")

    # Validator to capitalize species and location
    @validator('species', 'location')
    def capitalize(cls, value):
        if not value.istitle():
            raise ValueError(f"{value} must be capitalized.")
        return value

    # Validate date format
    @validator('date')
    def validate_date(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')  # No need to return a date object
            return value
        except ValueError:
            raise ValueError('Date must be in YYYY-MM-DD format.')

    # Validate time format
    @validator('time')
    def validate_time(cls, value):
        try:
            datetime.strptime(value, '%H:%M')  # No need to return a time object
            return value
        except ValueError:
            raise ValueError('Time must be in HH:MM format.')

# Create a new wildlife sighting
@app.post("/sightings", response_model=Sighting)
async def create_sighting(sighting: Sighting):
    if sighting.id in sightings_db:
        raise HTTPException(status_code=400, detail="Sighting ID already exists.")
    sightings_db[sighting.id] = sighting.dict()
    return sightings_db[sighting.id]

# Get all sightings or filter by species and location
@app.get("/sightings", response_model=List[Sighting])
async def read_sightings(species: Optional[str] = None, location: Optional[str] = None):
    filtered_sightings = [
        sighting for sighting in sightings_db.values()
        if (species.lower() in sighting["species"].lower() if species else True) and
           (location.lower() in sighting["location"].lower() if location else True)
    ]
    
    if not filtered_sightings:
        raise HTTPException(status_code=404, detail="No sightings found.")
    
    return filtered_sightings

# Get a specific sighting by ID
@app.get("/sightings/{sighting_id}", response_model=Sighting)
async def get_sighting_by_id(sighting_id: int):
    if sighting_id not in sightings_db:
        raise HTTPException(status_code=404, detail="Sighting not found.")
    
    return sightings_db[sighting_id]

# Update an existing sighting
@app.put("/sightings/{sighting_id}", response_model=Sighting)
async def update_sighting(sighting_id: int, updated_sighting: Sighting):
    if sighting_id not in sightings_db:
        raise HTTPException(status_code=404, detail="Sighting not found.")
    
    sightings_db[sighting_id].update({
        "species" :updated_sighting.species,
        "location": updated_sighting.location,
        "date": updated_sighting.date,
        "time": updated_sighting.time
    })
    
    return sightings_db[sighting_id]

# Delete a sighting by ID
@app.delete("/sightings/{sighting_id}", response_model=dict)
async def delete_sighting(sighting_id: int):
    if sighting_id not in sightings_db:
        raise HTTPException(status_code=404, detail="Sighting not found.")
    
    del sightings_db[sighting_id]
    return {"Message": "Sighting deleted successfully."}
