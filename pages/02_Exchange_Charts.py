import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load CSV data
@st.cache_data
def load_data():

    # Dataframe with the info from Kaggle exchange rates
    df_exchange = pd.read_csv('raw_data/kaggle.csv')
    df_exchange = df_exchange.drop('Unnamed: 0',axis=1)
    df_exchange = df_exchange[['timestamp','chinese_yuan_to_usd','brazilian_real_to_usd','russian_ruble_to_usd',
                              'south_african_rand_to_usd','indian_rupee_to_usd']]

    df_exchange.set_index('timestamp', inplace=True)

    # Handle missing values (backward fill)
    df_exchange.fillna(method='bfill', inplace=True)

    # Handle missing values (forward fill)
    df_exchange.fillna(method='ffill', inplace=True)

    return df_exchange

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
st.sidebar.title("Select your currency")
selected_features = st.sidebar.multiselect('Available currency', data.columns.tolist(), default=data.columns.tolist())

# Filter data based on selected features
filtered_data = data[selected_features]

# Plot time series
# st.title('Foreign exchange rates')
st.markdown('<div class="center"><p class="styled-text">FOREIGN EXCHANGE RATES</p></div>', unsafe_allow_html=True)
st.image('images/currency.png', width=150)
st.line_chart(filtered_data)
