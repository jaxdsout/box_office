import streamlit as st
import plotly.express as px
import pandas as pd
from loader import load_data
from datetime import date

path = "datasets"
df = load_data(path)

st.title("Box Office Data")

years = sorted(df['year'].unique(), reverse=True)
default_year_index = years.index('2024')

selected_year = st.selectbox(
    label="Year",
    options=years,
    index=default_year_index
)

filtered_df = df[df['year'] == selected_year]

figure = px.treemap(
    filtered_df,
    path=[px.Constant(selected_year), "title"],
    values='worldwide'
)

figure.update_traces(root_color="black")
figure.update_layout(margin=dict(t=50, l=25, r=25, b=25))

st.plotly_chart(
    figure,
    theme="streamlit"
)

# st.bar_chart(
#     filtered_df,
#     x='worldwide',
#     y='title'
# )


