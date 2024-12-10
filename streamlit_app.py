import streamlit as st
import numpy as np
import pandas as pd


st.title('⚽ Football Statistics App')
# Load the dataset from the URL
url = "https://www.kaggle.com/datasets/davidcariboo/player-scores/download/player_valuations.csv"
html = pd.read_html(url, header =1)
df = html[0]


