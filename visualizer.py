import streamlit as st
import pandas as pd
from loader import load_data

path = "datasets"
data = load_data(path)

st.title("Box Office Data")
