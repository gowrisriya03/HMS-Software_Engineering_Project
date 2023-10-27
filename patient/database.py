import mysql.connector

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@dbms@123",
    database="hms"
)

c = mydb.cursor()

def new_request(email, date_time):
    c.execute("INSERT INTO visits (patient_id, datetime) VALUES ((SELECT patient_id FROM patients WHERE email=%s), %s);", (email, date_time))
    mydb.commit()
    return

def history_db(email):
    c.execute("SELECT v.datetime, d.name, v.diagnose, v.review, v.prescription FROM visits as v, doctors as d WHERE patient_id=(SELECT patient_id FROM patients WHERE email=%s) AND d.doctor_id=v.doctor_id AND visit_done=1;", (email,))
    data = c.fetchall()
    return data

def get_doc_name_from_id(id):
    c.execute("SELECT name from doctors where doctor_id=%s", (id,))
    data=c.fetchall()
    name = data[0][0]
    return name

def appointments(email):
    c.execute("SELECT v.datetime, v.doctor_id FROM visits as v where patient_id=(SELECT patient_id FROM patients where email=%s) AND visit_done=0;", (email,))
    data = c.fetchall()
    return data