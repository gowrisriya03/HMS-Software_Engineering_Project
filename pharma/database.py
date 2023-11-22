import mysql.connector

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@dbms@123",
    database="hms"
)

c = mydb.cursor()

def provide(visit_id):
    c.execute("UPDATE visits SET pharmacy_done=1 WHERE visit_id=%s", (visit_id,))
    mydb.commit()
    return

def medicate_id_db():
    c.execute('SELECT visit_id FROM visits WHERE visit_done=1 AND pharmacy_done=0;')
    data = c.fetchall()
    result = [item[0] for item in data]
    return result

def medicate_db():
    c.execute('SELECT visit_id, p.name, prescription FROM visits as v, patients as p WHERE visit_done=1 AND pharmacy_done=0 AND p.patient_id=v.patient_id;')
    data = c.fetchall()
    return data