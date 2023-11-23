import streamlit as st
import pandas as pd

from doctor.database import appointments_db
from doctor.database import patient_details
from doctor.database import patient_history
from doctor.database import update_visit

def opd(email):
    appointments = appointments_db(email)
    ids = [tup[0] for tup in appointments]
    if len(ids)==0:
        st.divider()
        st.text("No OPD Request Available")
        return
    df = pd.DataFrame(appointments, columns=["Visit ID", "Date-Time", "Patient Name"])
    st.dataframe(df)
    visit_id = st.selectbox("Select Visit ID:", ids)

    st.divider()

    patientDetails = patient_details(visit_id)
    st.text("Patient ID: {}".format(patientDetails[0][0]))
    st.text("Patient Name: {}".format(patientDetails[0][1]))
    st.text("Patient Age: {}".format(patientDetails[0][2]))

    st.divider()

    patientHistory = patient_history(patientDetails[0][0])
    patientHistory_df = pd.DataFrame(patientHistory, columns=["Date-Time", "Doctor Name", "Diagnose", "Review", "Prescription"])
    if patientHistory_df.empty:
        st.text("No Patient History Available")
    else:
        st.text("Patient History:")
        st.dataframe(patientHistory_df)

    st.divider()

    diagnose = st.text_input("Diagnose:", key=1)
    review = st.text_input("Review:", key=2)
    prescription = st.text_input("Prescription:", key=3)
    if st.button("Finish OPD"):
        update_visit(visit_id, diagnose, review, prescription)
        st.success("Completed OPD for Visit ID: {}".format(visit_id))