import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='ML Model Building', page_icon='🤖')
st.title('🤖 ML Model Building')
uploaded_file = st.file_uploader("Upload a txt file", type=["txt"])
if uploaded_file is not None:
    df = pd.read_fwf(uploaded_file)
for d in df:
    st.write(d)

for i in range(len(df)):
    st.write(df[i])
    st.write(i)
