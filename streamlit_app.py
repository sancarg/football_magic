import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

st.title('⚽ Football Statistics App')
# Load the dataset from the URL
url = "https://www.kaggle.com/datasets/davidcariboo/player-scores/download/player_valuations.csv"
df = pd.read_csv(url)



