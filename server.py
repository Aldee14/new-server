from flask import Flask, render_template
import subprocess

app = Flask(__name__)

def run_cpp_executable(executable_name):
    try:
        result = subprocess.run(
            [f'bin/{executable_name}.exe'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stderr:
            return f"Error: {result.stderr}"
        return result.stdout
    except Exception as e:
        return f"Exception occurred: {str(e)}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_employee')
def add_employee():
    output = run_cpp_executable('add_employee')
    return render_template('add_employee.html', output=output)

@app.route('/update_employee')
def update_employee():
    output = run_cpp_executable('update_employee')
    return render_template('update_employee.html', output=output)

@app.route('/display_employees')
def display_employees():
    output = run_cpp_executable('display_employees')
    return render_template('display_employees.html', output=output)

@app.route('/log_attendance')
def log_attendance():
    output = run_cpp_executable('log_attendance')
    return render_template('log_attendance.html', output=output)

@app.route('/generate_payslip')
def generate_payslip():
    output = run_cpp_executable('generate_payslip')
    return render_template('generate_payslip.html', output=output)

@app.route('/remove_employee')
def remove_employee():
    output = run_cpp_executable('remove_employee')
    return render_template('remove_employee.html', output=output)

@app.route('/add_department')
def add_department():
    output = run_cpp_executable('add_department')
    return render_template('add_department.html', output=output)

@app.route('/update_department')
def update_department():
    output = run_cpp_executable('update_department')
    return render_template('update_department.html', output=output)

@app.route('/remove_department')
def remove_department():
    output = run_cpp_executable('remove_department')
    return render_template('remove_department.html', output=output)

@app.route('/display_departments')
def display_departments():
    output = run_cpp_executable('display_departments')
    return render_template('display_departments.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
