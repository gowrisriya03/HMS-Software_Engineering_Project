import streamlit as st
import pandas as pd

from pharma.database import medicate_id_db
from pharma.database import medicate_db
from pharma.database import provide

def medicate():
    st.subheader("Provide Medications:")
    ids = medicate_id_db()
    result = medicate_db()
    if len(ids)==0:
        st.text("No medications to be provided as of now")
    df = pd.DataFrame(result, columns=["Visit ID", "Patient", "Prescription"])
    st.dataframe(df)
    visit_id = st.selectbox("Visit ID:", ids)
    st.divider()
    if st.button("Provide Medicine to Visit ID: {}".format(visit_id)):
        provide(visit_id)
        st.success("Successfully Provided medicine to Visit ID: {}".format(visit_id))