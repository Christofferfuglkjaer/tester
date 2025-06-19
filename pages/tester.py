import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Define the required scopes
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]

# Load credentials from Streamlit secrets
skey = st.secrets["gcp_service_account"]
credentials = Credentials.from_service_account_info(
    skey,
    scopes=scopes,
)
client = gspread.authorize(credentials)

@st.cache_data(ttl=600)
def load_data(sheet_url, sheet_name="Ark1"):
    sh = client.open_by_url(sheet_url)
    worksheet = sh.worksheet(sheet_name)
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Example usage:
sheet_url = "https://docs.google.com/spreadsheets/d/1kw4gzt-Ybzkl2QVk9nU04yvCTBsJBqP6t7WYklwzSxg/edit?gid=0#gid=0"  # Replace with your actual Google Sheet URL
sheet_name = "Ark1"   # Replace with your worksheet name if different

df = load_data(sheet_url, sheet_name)
st.dataframe(df)