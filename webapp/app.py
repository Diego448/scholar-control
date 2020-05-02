from flask import Flask, render_template, request, redirect, url_for
import json, requests
from datetime import datetime, date, time
app = Flask(__name__)

restapi_url = 'http://127.0.0.1:5000/'
students_resource_url = restapi_url + 'students'
courses_resource_url = restapi_url + 'courses'
teachers_resource_url = restapi_url + 'teachers'
payments_resource_url = restapi_url + 'payments'

def get_students():
    r = requests.get('http://127.0.0.1:5000/students')
    return r.json()

def get_student_data(id):
    r = requests.get('http://127.0.0.1:5000/students/' + id)
    return r.json()

def add_student(data):
    headers = {
        'content-type': 'application/json'
    }
    requests.post('http://127.0.0.1:5000/students', json=data, headers=headers)

def update_student(student_id, student_etag, data):
    #current_data = get_student_data(student_id)
    #etag = current_data['_etag']
    headers = {
        'content-type': 'application/json', 
        'If-Match': str(student_etag)}
    requests.patch('http://127.0.0.1:5000/students/' + student_id, json=data, headers=headers)

def get_courses():
    r = requests.get(courses_resource_url)
    return r.json()

def get_course_data(id):
    r = requests.get(courses_resource_url + '/' + id)
    return r.json()

def add_course(data):
    headers = {'content-type': 'application/json'}
    r = requests.post(courses_resource_url, json=data, headers=headers)
    return r.status_code

def update_course(course_id, course_etag, data):
    headers = {'content-type': 'application/json', 'If-Match': str(course_etag)}
    r = requests.patch(courses_resource_url + '/' + course_id, json=data, headers=headers)
    return r.status_code

def get_status(data):
    if 'status' in data:
        return True
    else:
        return False

def get_formatted_date(date_string):
    new_date = date.fromisoformat(date_string)
    default_time = time(12, 00)       
    new_datetime = datetime.combine(new_date, default_time)
    return new_datetime.strftime("%a, %d %b %Y %H:%M:%S GMT")

def get_teachers():
    r = requests.get('http://127.0.0.1:5000/teachers')
    return r.json()

def get_teacher_data(id):
    r = requests.get(teachers_resource_url + '/' + id)
    return r.json()

def add_teacher(data):
    headers = {'content-type': 'application/json'}
    r = requests.post('http://127.0.0.1:5000/teachers', json=data, headers=headers)
    return r.status_code

def update_teacher(teacher_id, teacher_etag, data):
    headers = {'content-type': 'application/json', 'If-Match': str(teacher_etag)}
    r = requests.patch(teachers_resource_url + '/' + teacher_id, json=data, headers=headers)
    return r.status_code

def get_teacher_courses(teacher_id):
    r = requests.get(courses_resource_url + '?where={"teacher":"' + str(teacher_id) + '"}')
    return r.json()

def get_payments():
    r = requests.get(payments_resource_url)
    return r.json()

def get_payment_data(id):
    r = requests.get(payments_resource_url + '/' + id)
    return r.json()

def add_payment(data):
    headers = {'content-type': 'application/json'}
    r = requests.post(payments_resource_url, json=data, headers=headers)
    return r.status_code

def get_student_payments(student_id):
    r = requests.get(payments_resource_url + '?where={"student":"' + str(student_id) + '"}')
    return r.json()

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

@app.route('/edit/student/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if request.method == 'POST':
        updated_data = {'firstname': request.form['firstname'], 'lastname': request.form['lastname'], 
        'location': request.form['location'], 'phone_number': request.form['phone_number'], 
        'status': get_status(request.form)}
        update_student(student_id, request.form['etag'], updated_data)
        return redirect(url_for('student_directory'))
    student_data = get_student_data(student_id)
    return render_template("edit_student.html", student_data=student_data)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html"), 404

@app.route('/directory/courses')
def courses_directory(courses={}):
    courses_data = get_courses()
    return render_template("courses_directory.html", courses=courses_data['_items'])

@app.route('/add/course', methods=['GET', 'POST'])
def create_course():
    if request.method == 'POST':
        new_course = {"name": request.form['name'], "teacher": request.form['teacher'],
        "start":  get_formatted_date(request.form['start']), 
        "end": get_formatted_date(request.form['end']), "cost": request.form['cost'],
        "status": request.form['status']}
        add_course(new_course)
        return redirect(url_for('courses_directory'))
    teachers = get_teachers()
    return render_template("add_course.html", teachers=teachers['_items'])

@app.route('/edit/course/<course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    if request.method == 'POST':
        updated_course = {"name": request.form['name'], "teacher": request.form['teacher'],
        "start":  get_formatted_date(request.form['start']), 
        "end": get_formatted_date(request.form['end']), "cost": request.form['cost'],
        "status": request.form['status']}
        update_course(course_id, request.form['etag'], updated_course)
        return redirect(url_for('courses_directory'))
    course_data = get_course_data(course_id)
    teachers = get_teachers()
    return render_template("edit_course.html", course_data=course_data, teachers=teachers['_items'])

@app.template_filter('toisoformat')
def toisoformat(input_string):
    if input_string:
        input_datetime = datetime.strptime(input_string, '%a, %d %b %Y %H:%M:%S GMT')
        return input_datetime.strftime('%Y-%m-%d')
    return "Fecha no asignada"

@app.route('/directory/teachers')
def teachers_directory():
    teachers_data = get_teachers()
    return render_template("teacher_directory.html", teachers=teachers_data['_items'])

@app.route('/add/teacher', methods=['GET', 'POST'])
def add_teachers():
    if request.method == 'POST':
        new_teacher = {'firstname': request.form['firstname'], 'lastname': request.form['lastname'],
        'students_number': request.form['students_number'], 'phone_number': request.form['phone_number'],
        'status': request.form['status']}
        add_teacher(new_teacher)
        return redirect(url_for('teachers_directory'))
    return render_template("add_teacher.html")

@app.route('/edit/teacher/<teacher_id>', methods=['GET', 'POST'])
def edit_teacher(teacher_id):
    if request.method == 'POST':
        updated_data = {'firstname': request.form['firstname'], 'lastname': request.form['lastname'], 
        'phone_number': request.form['phone_number'], 'status': request.form['status']}
        update_teacher(teacher_id, request.form['etag'], updated_data)
        return redirect(url_for('teachers_directory'))
    teacher_data = get_teacher_data(teacher_id)
    return render_template("edit_teacher.html", teacher_data=teacher_data)

@app.route('/directory/courses/<teacher_id>')
def teacher_courses(teacher_id):
    courses = get_teacher_courses(teacher_id)
    return render_template("teacher_courses.html", courses=courses['_items'])

@app.route('/registry/payments')
def payments_registry():
    payments = get_payments()
    return render_template("payment_registry.html", payments=payments['_items'])

@app.route('/add/payment', methods=['GET', 'POST'])
def register_payment():
    if request.method == 'POST':
        new_payment = {'course': request.form['course'], 'student': request.form['student'],
        'amount': request.form['amount'], 
        'payment_date': get_formatted_date(request.form['payment_date'])}
        add_payment(new_payment)
        return redirect(url_for('payments_registry'))
    students = get_students()
    courses = get_courses()
    return render_template("add_payment.html", students=students['_items'], courses=courses['_items'])

@app.route('/registry/payments/<student_id>')
def student_payments(student_id):
    payments = get_student_payments(student_id)
    unique_courses = set(entry['course'] for entry in payments['_items'])
    courses = list(entry['course'] for entry in payments['_items'])
    summary = []
    for value in unique_courses:
        entry = {}
        entry['amount'] = courses.count(value)
        entry['course'] = value
        summary.append(entry)
    return render_template("student_payments.html", payments=payments['_items'], student=student_id, summary=summary)

@app.route('/enroll/student/<student_id>', methods=['GET', 'POST'])
def enroll_student(student_id):
    if request.method == 'POST':
        course_id = request.form['course']
        course = get_course_data(course_id)
        student_list = course['students']
        student_list.append(student_id)
        update_data = {"students": student_list}
        update_course(course_id, course['_etag'], update_data)
        return redirect(url_for('student_directory'))
    courses = get_courses()    
    return render_template("enroll_student.html", courses=courses['_items'])

@app.route('/directory/courses/enrolled/<course_id>/')
def enrolled_students(course_id):
    course_data = get_course_data(course_id)
    student_list = course_data['students']
    return render_template("enrolled_students.html", students=student_list)