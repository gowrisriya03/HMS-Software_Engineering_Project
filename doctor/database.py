import mysql.connector

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@dbms@123",
    database="hms"
)

c = mydb.cursor()

def update_visit(visit_id, diagnose, review, prescription):
    c.execute("UPDATE visits SET visit_done=1, diagnose=%s, review=%s, prescription=%s WHERE visit_id=%s",(diagnose, review, prescription, visit_id))
    mydb.commit()
    return

def patient_history(patient_id):
    c.execute("SELECT v.datetime, d.name, v.diagnose, v.review, v.prescription FROM visits as v, doctors as d WHERE d.doctor_id=v.doctor_id AND patient_id=%s AND visit_done=1", (patient_id,))
    data = c.fetchall()
    return data

def patient_details(visit_id):
    c.execute("SELECT patient_id, name, age FROM patients WHERE patient_id=(SELECT patient_id FROM visits WHERE visit_id=%s)", (visit_id,))
    data = c.fetchall()
    return data

def appointments_db(email):
    c.execute("SELECT v.visit_id, v.datetime, p.name FROM visits as v, patients as p WHERE v.doctor_id=(SELECT doctor_id FROM doctors WHERE email=%s) AND v.visit_done=0 AND p.patient_id=v.patient_id", (email, ))
    data = c.fetchall()
    return data

def approve(id, email):
    c.execute("UPDATE visits SET doctor_id=(SELECT doctor_id FROM doctors WHERE email=%s) WHERE visit_id=%s;", (email, id))
    mydb.commit()
    return

def reject(id):
    c.execute("DELETE FROM visits WHERE visit_id=%s", (id,))
    mydb.commit()
    return


def new_requests_db():
    c.execute("SELECT visit_id, datetime, patient_id FROM visits WHERE doctor_id IS NULL;")
    data = c.fetchall()
    return data