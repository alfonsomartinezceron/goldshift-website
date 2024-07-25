import streamlit as st
import requests
import numpy as np
import pandas as pd
import matplotlib as plt
#from PIL import Image
import requests
#from io import BytesIO

# Function to interact with FastAPI backend
def get_prediction():
    url = f"https://goldshift-usqqma72oq-ew.a.run.app/predict"
    response = requests.get(url)
    return response.json()

st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .styled-text {
        font-size: 40px;  /* Adjust the size as needed */
        color: "#000000";  /* Replace with your desired color */
        font-weight: bold;  /* Make the text bold */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="center"><p class="styled-text">GOLDSHIFT - GOLD PREDICTION</p></div>', unsafe_allow_html=True)
#st.title("Gold price prediction for tomorrow")

st.write("Click on the button below to see tomorrow's predicted price of gold!")
if st.button("Gold Prediction"):
    result = get_prediction()['day 1']
    st.write(f"__Tomorrow, gold will be valued at: {result:.2f} USD__")

st.image('images/liquid_gold.jpg', width=600)
