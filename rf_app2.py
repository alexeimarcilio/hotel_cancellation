import streamlit as st
import pickle

# Load the model
with open('rf_model_conversion_new.sav', 'rb') as f:
    model = pickle.load(f)

# Define the slider widgets
params = {}
params['lead_time'] = st.sidebar.slider('Lead Time', min_value=0, max_value=500, value=50)
params['avg_price_per_room'] = st.sidebar.slider('Average Price per Room', min_value=0, max_value=1000, value=200)
params['no_of_special_requests'] = st.sidebar.slider('Number of Special Requests', min_value=0, max_value=5, value=1)
params['no_of_week_nights'] = st.sidebar.slider('Number of Week Nights', min_value=0, max_value=10, value=2)
params['no_of_weekend_nights'] = st.sidebar.slider('Number of Weekend Nights', min_value=0, max_value=10, value=2)

# Make the prediction and display the result
prediction = model.predict([[params['lead_time'], params['avg_price_per_room'], params['no_of_special_requests'], params['no_of_week_nights'], params['no_of_weekend_nights']]])


# Add a title to the app
st.title("Hilton Hotel Cancellation Predictor")

if prediction[0] == 0:
    st.markdown("<h1 style='text-align: center; color: red;'>Cancelled</h1>", unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center; color: green;'>Not Cancelled</h1>", unsafe_allow_html=True)

# Add your name and today's date to the title
st.markdown("<h2 style='text-align: center; color: black;'>by Alexei Marcilio, 23 April 2023</h2>", unsafe_allow_html=True)

