from flask import Flask, render_template
import json, requests
app = Flask(__name__)

def get_students():
    r = requests.get('http://127.0.0.1:5000/students')
    return r.json()

@app.route('/student_control')
def student_control(students={}):
    students_data = get_students()
    return render_template("student_control.html", students=students_data['_items'])