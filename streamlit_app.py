import streamlit as st
import numpy as np
import pandas as pd
import os

st.title('⚽ Football Statistics App')
# Load the dataset from the URL
# Get Kaggle credentials from Streamlit Secrets

df = pd.read_csv("https://sports-statistics.com/sports-data/fifa-2022-dataset-csvs/players_22.csv")



