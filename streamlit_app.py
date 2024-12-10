import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Ensure Kaggle credentials are set up 
os.environ['KAGGLE_CONFIG_DIR'] = "/root/.kaggle"

# Download the dataset from Kaggle 
kaggle datasets download -d davidcariboo/player-scores

st.title('⚽ Football Statistics App')



