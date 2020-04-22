from flask import Flask
app = Flask(__name__)

@app.route('/student_control')
def student_control():
    return render_template("student_control.html")