import streamlit as st
import pandas as pd
import gspread
import matplotlib.pyplot as plt
from google.oauth2.service_account import Credentials
from datetime import datetime

# ---- Google Sheets Setup ----
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
skey = st.secrets["gcp_service_account"]
credentials = Credentials.from_service_account_info(skey, scopes=scopes)
client = gspread.authorize(credentials)

# ---- Load Data ----
url = st.secrets["gcp_service_account"]["spreadsheet"]
sheet_name = "ryg"
sheet = client.open_by_url(url).worksheet(sheet_name)

# Read data into DataFrame
@st.cache_data(ttl=600)
def load_data():
    return pd.DataFrame(sheet.get_all_records())

df = load_data()
st.subheader("Current Data")

def row_merger(df):
    df = df.copy()
    for i in range(len(df)):
        if df.loc[i, 'Pull Ups'] == 0:
            df.loc[i, 'Pull Ups'] = df.loc[i, 'Rows']
        elif df.loc[i, 'Rows'] == 0:
            df.loc[i, 'Rows'] = df.loc[i, 'Pull Ups']
    return df


# Page title
st.title("Fremgang Plots")
# Create tabs for different plots
ryg, bryst, random, arme = st.tabs(["Ryg", "Bryst", "Random", "Arme"])

with ryg:
    df = load_data()
    st.dataframe(df)
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    st.write(df)
    # make so that pull ups and rows are on one line given the date
    df = row_merger(df)
    st.write(df)
    st.subheader("Current Data")
    st.markdown("### Add Rows")
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Rows'], marker='o', label='Rows')
    plt.xlabel("Date")
    plt.ylabel("Rows")
    plt.title("Rows Over Time")
    plt.legend()
    st.pyplot(plt)
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Pull Ups'], marker='o', label='Pull Ups', color='orange')
    plt.xlabel("Date")
    plt.ylabel("Pull Ups")
    plt.title("Pull Ups Over Time")
    plt.legend()
    st.pyplot(plt)
