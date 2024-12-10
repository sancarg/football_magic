import streamlit as st
import altair as alt
import plotly.express as px
import pandas as pd

from utils import load_td

st.set_page_config(
    layout="wide",
    page_title="About",
    page_icon="👋"
)
