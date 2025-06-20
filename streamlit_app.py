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

# ---- Load Sheet ----
url = st.secrets["gcp_service_account"]["spreadsheet"]
sheet_name = "ryg"
sheet = client.open_by_url(url).worksheet(sheet_name)

# ---- Load Data into DataFrame ----
@st.cache_data(ttl=600)
def load_data():
    return pd.DataFrame(sheet.get_all_records())

df = load_data()
st.dataframe(df)

# ---- Tabs ----
ryg, bryst, random, arme = st.tabs(["Ryg", "Bryst", "Random", "Arme"])

with ryg:
    st.subheader("Current Data")
    # ---- Add Rows Input ----
    st.markdown("### Add Rows")
    col1, col2, col3 = st.columns([3, 3, 1])
    with col1:
        rows = st.number_input("Rows", min_value=0, value=0, key="rows_input")
    with col2:
        reps = st.number_input("Reps", min_value=0, value=0, key="reps_input")
    with col3:
        if st.button("Submit Rows", key="rows_submit"):
            rows_val = rows * reps
            new_row = [
                datetime.now().strftime("%Y-%m-%d"),
                None,
                rows_val
            ]
            sheet.append_row(new_row)
            st.success("Row added! Please refresh to see it.")

    # ---- Add Pull Ups Input ----
    st.markdown("### Add Pull Ups")
    col4, col5, col6 = st.columns([3, 3, 1])
    with col4:
        pull_ups = st.number_input("Pull Ups", min_value=0, value=0, key="pull_ups_input")
    with col5:
        pull_ups_reps = st.number_input("Reps", min_value=0, value=0, key="pull_ups_reps_input")
    with col6:
        if st.button("Submit Pull Ups", key="pull_ups_submit"):
            pull_ups_val = pull_ups * pull_ups_reps
            new_row = [
                datetime.now().strftime("%Y-%m-%d"),
                pull_ups_val,
                None
            ]
            sheet.append_row(new_row)
            st.success("Pull ups added! Please refresh to see it.")
