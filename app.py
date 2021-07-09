import streamlit as st
import requests
import datetime

'''
# TaxiFare Predictions
'''

'''
## Select the parameters of the ride
'''

d = st.date_input(
    "Pickup Date",
    datetime.date(2021, 1, 1))

t = st.time_input('Pickup Time', datetime.time(8, 45))

pickup_datetime = f'{d} {t}'

#st.write('Chosen datetime:', pickup_datetime)


pickup_longitude = st.number_input('pickup longitude: ', value=40.7614327)
pickup_latitude = st.number_input('pickup latitude: ', value=-73.9798156)

#st.write('The current pickup location is: ', ("lon: " + str(pickup_longitude) + ",  " + "lat:  + str(pickup_latitude)))

dropoff_longitude = st.number_input('dropoff longitude: ', value=40.6413111)
dropoff_latitude = st.number_input('dropoff latitude: ', value=-73.7803331)

#st.write('The current dropoff location is: ', ("lon: " + str(dropoff_longitude) + ",  " + "lat: " + str(dropoff_latitude)))

passenger_count = st.slider('Number of Passengers: ', min_value=1, max_value=8, value=2, step=1)

#st.write('Current # passengers: ', passenger_count)


url = 'https://taxifare-api-dsvsmf3mja-de.a.run.app/predict'


params = {"pickup_datetime": pickup_datetime,
          "pickup_longitude": pickup_longitude,
          "pickup_latitude": pickup_latitude,
          "dropoff_longitude": dropoff_longitude,
          "dropoff_latitude": dropoff_latitude,
          "passenger_count": passenger_count}

response = requests.get(url, params=params).json()

prediction = round(response['prediction'], 2)

'''
## Prediction:
'''
f"$ {prediction}"






