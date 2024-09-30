import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("D:\\Programming\\PYTHON\\PROJECT\\AAS\\serviceAccKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' :"https://attendance-systemaas-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "963852":{
        "Name" : "Elon Musk",
        "Age" : "50",
        "Branch" : "B.tech",
        "Year" : "4",
        "Last-Attendance" : "2024-09-12 00:54:34",
        "Total-Attendance" : "5",
        "Starting-year" : "2021"

    },
    
    "852741":{
        "Name" : "Emily Blunt",
        "Age" : "30",
        "Branch" : "BCA",
        "Year" : "2",
        "Last-Attendance" : "2024-09-12 00:54:34",
        "Total-Attendance" : "5",
        "Starting-year" : "2021"

    }
}

for key,value in data.items():
    ref.child(key).set(value)