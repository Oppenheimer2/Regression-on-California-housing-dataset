import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pickled model
model = pickle.load(open("ridge.pkl", "rb"))

# Streamlit app title
st.title("California Housing Price Prediction")

# Sidebar with user input
st.sidebar.header("User Input")
def get_user_input():
    # Default values for input fields
    med_inc = st.sidebar.slider("Median Income (scaled)", 0.1, 15.0, 3.0)
    housing_med_age = st.sidebar.slider("Housing Median Age", 1, 52, 20)
    avg_rooms = st.sidebar.slider("Average Rooms", 1, 10, 5)
    avg_bedrooms = st.sidebar.slider("Average Bedrooms", 1, 10, 5)
    population = st.sidebar.slider("Population (scaled)", 100, 10000, 1000)
    households = st.sidebar.slider("Households", 1, 6082, 500)
    latitude = st.sidebar.slider("Latitude", 32.54, 41.95, 37.75)
    longitude = st.sidebar.slider("Longitude", -124.35, -114.31, -119.80)

    # Create a dictionary to hold user input values
    user_data = {
        "median_income": med_inc,
        "housing_median_age": housing_med_age,
        "average_rooms": avg_rooms,
        "average_bedrooms": avg_bedrooms,
        "population": population,
        "households": households,
        "latitude": latitude,
        "longitude": longitude,
    }
    return user_data

# Get user input
user_input = get_user_input()

# Create a DataFrame from the user input
input_df = pd.DataFrame([user_input])

# Predict housing price
price = model.predict(input_df)
# Display the result
st.subheader("Predicted Housing Price")
st.write(f"${price[0]:,.2f}")

# You can also display additional information about the input data if needed
st.subheader("User Input:")
st.write(user_input)

# Optionally, display a map of the region based on the provided latitude and longitude
st.map((user_input['latitude'], user_input['longitude']))