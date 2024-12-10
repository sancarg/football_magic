import streamlit as st
import numpy as np
import pandas as pd
import os

st.title('⚽ Football Statistics App')
# Load the dataset from the URL
# Get Kaggle credentials from Streamlit Secrets
os.environ['GSancar'] = st.secrets["credentials"]["GSancar"]
#url = "https://www.kaggle.com/datasets/davidcariboo/player-scores/download/player_valuations.csv"



