import streamlit as st
import numpy as np
import pandas as pd
import os

st.title('⚽ Football Statistics App')
# Load the dataset from the URL 
url = "https://sports-statistics.com/sports-data/fifa-2022-dataset-csvs/players_22.csv" 
df = pd.read_csv(url)


