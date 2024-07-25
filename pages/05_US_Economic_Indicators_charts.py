import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#from PIL import Image
import requests
#from io import BytesIO

@st.cache_data
def load_data():
    # Dataframe with the info from API Alpha commodities
    df_alpha = pd.read_csv('raw_data/alpha.csv')
    df_alpha = df_alpha.drop('Unnamed: 0',axis=1)
    df_alpha = df_alpha.drop(columns= ['BRENT','WTI','NATURAL_GAS','TREASURY_YIELD'])
    #df_alpha = df_alpha.drop(columns= ['BRENT'])
    df_alpha = df_alpha.replace('.', np.nan)
    listcols=['FEDERAL_FUNDS_RATE']
    #listcols=['WTI','FEDERAL_FUNDS_RATE','NATURAL_GAS','TREASURY_YIELD']
    for col in listcols:
        df_alpha[col] = pd.to_numeric(df_alpha[col],downcast = 'float')

    df_alpha.set_index('timestamp', inplace=True)

    # Handle missing values (backward fill)
    df_alpha.fillna(method='bfill', inplace=True)

    # Handle missing values (forward fill)
    df_alpha.fillna(method='ffill', inplace=True)

    return df_alpha

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
st.sidebar.title("Select your US economic indicator")
selected_features = st.sidebar.multiselect('Economic factor', data.columns.tolist(), default=data.columns.tolist())

# Filter data based on selected features
filtered_data = data[selected_features]

# Plot time series
#st.title('US economic indicators')
st.markdown('<div class="center"><p class="styled-text">US ECONOMIC INDICATORS</p></div>', unsafe_allow_html=True)
st.image('images/flag_usa.png', width=200)
st.line_chart(filtered_data)
