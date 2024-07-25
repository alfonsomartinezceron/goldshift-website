import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    # Dataframe with gold prices
    df_gold = pd.read_csv('raw_data/gold_usd.csv')
    df_gold = df_gold.drop('Unnamed: 0',axis=1)

    #Adding a % column to gold price variation between T and T-1
    #df_gold['gold_old'] = df_gold['gold_price'].shift(1)
    #df_gold['gold_change'] = ((df_gold['gold_price'] - df_gold['gold_old']) / df_gold['gold_old']) * 100
    #df_gold.drop('gold_old', axis=1, inplace=True)

    df_gold.set_index('timestamp', inplace=True)

    # Handle missing values (backward fill)
    df_gold.fillna(method='bfill', inplace=True)

    # Handle missing values (forward fill)
    df_gold.fillna(method='ffill', inplace=True)

    # Create lagged features
    #for col in data.columns:
    #    for lag in range(1, 6):  # 1 to 5 days lag
    #        data[f'{col}_lag{lag}'] = data[col].shift(lag)

    # Drop rows with NaN values created by lagging
    #df.dropna(inplace=True)

    return df_gold

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
st.sidebar.title("Select gold parameter")
selected_features = st.sidebar.multiselect('Gold parameter', data.columns.tolist(), default=data.columns.tolist())

# Filter data based on selected features
filtered_data = data[selected_features]

# Plot time series
#st.title('Gold price')
st.markdown('<div class="center"><p class="styled-text">GOLD PRICE</p></div>', unsafe_allow_html=True)
st.image('images/gold.jpg', width=300)
st.line_chart(filtered_data)
st.image('images/gold_production.png', width=500)
