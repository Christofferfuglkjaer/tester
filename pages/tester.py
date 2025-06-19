import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.write(st.__version__)
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read( )

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")