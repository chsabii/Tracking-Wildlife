import streamlit as st
import requests
from datetime import datetime

# Set the FastAPI backend URL
API_URL = "http://localhost:8000/sightings/"

st.set_page_config(
    layout="wide",
    page_title="Wildlife Sighting Tracker",
    page_icon="",
    initial_sidebar_state="auto"
)

st.header("Wildlife Sighting Tracker")
st.image("C:\\\\Users\\\\Sabii\\\\OneDrive\\\\Desktop\\\\RIVON\\\\LEARNING FASTAPI\\\\version_2\\\\tiger_trail_garden_hero.jpg", 
         width=1100, 
         use_column_width=True, 
         output_format="JPEG")

choice = st.selectbox(
    "Choose an action", 
    ["Submit a New Sighting", "View All Sightings", "Search Sightings", "Update Sighting", "Delete Sighting"]
)


# Function to submit data to the FastAPI backend
def submit_sighting(species, location, date, time):
    data = {
        "species": species, 
        "location": location,
        "date": date.strftime("%Y-%m-%d"),
        "time": time.strftime("%H:%M")
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        st.success("🎉 Sighting submitted successfully!")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")

# Function to retrieve and display all sightings
def get_sightings():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error retrieving sightings.")
        return []

# Function to search for sightings based on species or location
def search_sightings(species, location):
    params = {}
    if species:
        params['species'] = species
    if location:
        params['location'] = location
    response = requests.get(f"{API_URL}search/", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error searching for sightings.")
        return []

# Function to update a sighting by ID
def update_sighting(sighting_id, species, location, date, time):
    data = {
        "species": species, 
        "location": location,
        "date": date.strftime("%Y-%m-%d"),
        "time": time.strftime("%H:%M")
    }
    response = requests.put(f"{API_URL}{sighting_id}", json=data)
    if response.status_code == 200:
        st.success(f"Sighting {sighting_id} updated successfully!")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")

# Function to delete a sighting by ID
def delete_sighting(sighting_id):
    response = requests.delete(f"{API_URL}{sighting_id}")
    if response.status_code == 200:
        st.success(f"Sighting {sighting_id} deleted successfully!")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")

# Based on the user's choice, show the corresponding form
if choice == "Submit a New Sighting":
    # Input fields for species, location, date, and time
    species = st.text_input("🔍 Species Name", "")
    location = st.text_input("📍 Location", "")
    sighting_date = st.date_input("📅 Date of Sighting", value=datetime.today())
    sighting_time = st.time_input("⏰ Time of Sighting", value=datetime.now().time())

    # Button to submit the form
    if st.button("Submit Sighting"):
        if species and location:
            submit_sighting(species, location, sighting_date, sighting_time)
        else:
            st.error("Please fill out all fields.")

elif choice == "View All Sightings":
    # Show all existing sightings
    st.subheader("📑 Existing Sightings")
    sightings = get_sightings()

    if sightings:
        for sighting_id, sighting_details in sightings.items():
            st.write(f"{sighting_id}: {sighting_details}")
    else:
        st.write("No sightings found.")

elif choice == "Search Sightings":
    species_search = st.text_input("Search by Species Name", "")
    location_search = st.text_input("Search by Location", "")
    
    if st.button("Search"):
        sightings = search_sightings(species_search, location_search)
        if sightings:
            for sighting_id, sighting_details in sightings.items():
                st.write(f"{sighting_id}: {sighting_details}")
        else:
            st.write("No sightings found.")

elif choice == "Update Sighting":
    sighting_id = st.number_input("Enter Sighting ID to Update", min_value=1, step=1)
    species = st.text_input("New Species Name", "")
    location = st.text_input("New Location", "")
    sighting_date = st.date_input("New Date of Sighting", value=datetime.today())
    sighting_time = st.time_input("New Time of Sighting", value=datetime.now().time())

    if st.button("Update Sighting"):
        if sighting_id and species and location:
            update_sighting(sighting_id, species, location, sighting_date, sighting_time)
        else:
            st.error("Please fill out all fields.")

elif choice == "Delete Sighting":
    sighting_id = st.number_input("Enter Sighting ID to Delete", min_value=1, step=1)
    
    if st.button("Delete Sighting"):
        if sighting_id:
            delete_sighting(sighting_id)
        else:
            st.error("Please enter a valid Sighting ID.")
