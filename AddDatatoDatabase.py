import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-a1744-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')
   
data = {
    "20011216":
        {
            "name": "Kritagya Painuly",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20011217":
        {
            "name": "Drishti Painuly",
            "major": "Agriculture",
            "starting_year": 2023,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20011218":
        {
            "name": "Yukti Bisht",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }     

}

for key, value in data.items():
    ref.child(key).set(value)