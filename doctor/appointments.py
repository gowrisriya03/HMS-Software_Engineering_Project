import streamlit as st
import pandas as pd

from doctor.database import appointments_db

def appointments(email):
    result = appointments_db(email)
    df = pd.DataFrame(result, columns=["Visit ID", "Date-Time", "Patient Name"])
    if df.empty:
        st.divider()
        st.text("You dont have any scheduled appointments")
        return
    st.divider()
    st.dataframe(df)