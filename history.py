import streamlit as st
import pandas as pd

from patient.database import history_db

def history(email):
    result = history_db(email)
    df = pd.DataFrame(result, columns=["Date-Time", "Doctor Name", "Diagnose", "Review", "Prescription"])
    if df.empty:
        st.markdown(":red[You dont have any medical history with us]")
        return
    st.dataframe(df)
    return