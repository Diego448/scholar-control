from flask import Flask, render_template
app = Flask(__name__)

@app.route('/student_control')
def student_control(students={}):
    return render_template("student_control.html")