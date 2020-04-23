from flask import Flask, render_template, request, redirect, url_for
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

<<<<<<< HEAD
def update_student(student_id, data):
    headers = {
        'content-type': 'application/json', 
        'If-Match': str(etag)}
    requests.patch('http://127.0.0.1:5000/students/' + student_id, json=data, headers=headers)
=======
def get_status(data):
    if 'status' in data:
        return True
    else:
        return False
>>>>>>> baa3f85b436b4494dd9c3a5a60803b9110d30dd5

@app.route('/directory/students')
def student_directory(students={}):
    students_data = get_students()
    return render_template("student_directory.html", students=students_data['_items'])

@app.route('/add/student', methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':
        new_student = {'firstname': request.form['firstname'], 'lastname': request.form['lastname'],
        'location': request.form['location'], 'phone_number': request.form['phone_number'],
        'status': get_status(request.form)}
        add_student(new_student)
        return redirect(url_for('student_directory'))
    return render_template("add_student.html")

@app.route('/edit/student/<student_id>')
def edit_student(student_id):
    return student_id