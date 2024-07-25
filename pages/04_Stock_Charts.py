import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# Function to load CSV data
@st.cache_data
def load_data():
    # Dataframe with the info from API Alpha gold companies
    df_stock = pd.read_csv('raw_data/stock.csv')
    df_stock = df_stock.drop('Unnamed: 0',axis=1)
    #df_stock = df_stock[['timestamp','GOLD','BVN','GFI']]
    df_stock = df_stock[['timestamp','NEM','KGC','HMY','CDE']]

    df_stock.set_index('timestamp', inplace=True)

    # Handle missing values (backward fill)
    df_stock.fillna(method='bfill', inplace=True)

    # Handle missing values (forward fill)
    df_stock.fillna(method='ffill', inplace=True)

    return df_stock

data = load_data()

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

# Sidebar for feature selection
st.sidebar.title("Select your stock (NYSE)")
selected_features = st.sidebar.multiselect('Available stocks', data.columns.tolist(), default=data.columns.tolist())

# Filter data based on selected features
filtered_data = data[selected_features]

# Plot time series
# st.title('Stock price of gold companies')
st.markdown('<div class="center"><p class="styled-text">STOCK PRICE OF GOLD COMPANIES</p></div>', unsafe_allow_html=True)
st.image('images/nyse.jpg', width=200)
st.line_chart(filtered_data)
