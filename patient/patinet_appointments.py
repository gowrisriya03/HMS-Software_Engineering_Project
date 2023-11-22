import streamlit as st
from datetime import datetime

from patient.database import appointments
from patient.database import new_request
from patient.database import get_doc_name_from_id

def patinet_appointments(email):
    result = appointments(email)

    if len(result)==0:
        st.subheader('New Appointment:')
        st.divider()
        date = st.date_input("Enter Date")
        time = st.time_input('Enter Time')
        date_time = datetime.combine(date, time)
        if st.button("Request Appointment"):
            new_request(email, date_time)
            st.success("Appointment Request Successfully")
    
    else:
        st.subheader("Your Appointment:")
        st.divider()
        st.markdown(":blue[Date:] {}".format((str(result[0][0]))[0:10]))
        st.markdown(":blue[Time:] {}".format((str(result[0][0]))[11:]))
        if result[0][1]==None:
            st.markdown(":red[Your appointment is not yet approved by any Doctor]")
        else:
            st.markdown("Your appointment is :green[approved] by :orange[{}]".format(get_doc_name_from_id(result[0][1])))