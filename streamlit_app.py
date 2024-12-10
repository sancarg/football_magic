import streamlit as st
import numpy as np
import pandas as pd
import os

# Set the page configuration 
st.set_page_config(page_title="Movie Insights Analyzer", page_icon="📽", layout="wide")

st.title('⚽ Football Statistics App')
# Load the dataset from the URL 
df = pd.read_csv('players_22.csv')
st.dataframe(df.head())


