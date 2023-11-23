import streamlit as st
import pandas as pd

from doctor.database import new_requests_db
from doctor.database import approve
from doctor.database import reject

def new_requests(email):
    result = new_requests_db()
    ids = [tup[0] for tup in result]
    if len(ids)==0:
        st.text("No new appointment requests")
        return
    df = pd.DataFrame(result, columns=["Visit Id", "Date-Time", "Patient ID"])
    st.text("New Appointments:")
    st.dataframe(df)
    st.divider()
    id = st.selectbox("Visit ID:", ids)
    if st.button("Approve"):
        approve(id, email)
        st.success("Successfully Approved Visit ID: {}".format(id))
    if st.button("Reject"):
        reject(id)
        st.success("Successfully Approved Visit ID: {}".format(id))
