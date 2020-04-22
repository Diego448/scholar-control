from flask import Flask, render_template
import json, requests
app = Flask(__name__)

def get_students():
    r = requests.get('http://127.0.0.1:5000/students')
    return r.json()

def add_student(data):
    headers = {
        'content-type': 'application/json'
    }
    requests.post('http://127.0.0.1:5000/students', json=data, headers=headers)

@app.route('/directory/students')
def student_directory(students={}):
    students_data = get_students()
    return render_template("student_directory.html", students=students_data['_items'])