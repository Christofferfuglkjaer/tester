import streamlit as st
import pandas as pd
import gspread
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
st.write(df)

# ---- Input Fields for New Row ----
st.subheader("Add New Entry")
col1, col2 = st.columns(2)

with col1:
    pull_ups = st.number_input("Pull Ups", min_value=0, value=0)
with col2:
    rows = st.number_input("Rows", min_value=0, value=0)

if st.button("Add Row"):
    # Prepare new row (must match header order!)
    new_row = [
        datetime.now().strftime("%Y-%m-%d"),
        pull_ups if pull_ups > 0 else None,
        rows if rows > 0 else None
    ]

    # Append the row
    sheet.append_row(new_row)
    st.success("Row added! Please refresh to see it.")
