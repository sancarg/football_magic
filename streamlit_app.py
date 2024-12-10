import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import os
# Ensure Kaggle credentials are set up 
os.environ['KAGGLE_CONFIG_DIR'] = "/root/.kaggle"

# Download the dataset from Kaggle 
!kaggle datasets download -d davidcariboo/player-scores

st.title('⚽ Football Statistics App')



