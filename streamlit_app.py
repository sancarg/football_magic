import streamlit as st
import numpy as np
import pandas as pd
import os

st.title('⚽ Football Statistics App')
# Load the dataset from the URL 
df = pd.read_csv('https://github.com/abineshta/FIFA-22-complete-player-dataset-EDA/blob/main/players_22.csv')


