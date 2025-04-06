from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

# Define the path to your SQLite database file
DATABASE = 'db/registration_system.db'

'''
API Calls will always return a json with these key/value pairs. The values will represent the state of the database
after the command has been completed. 

The "status" field will always be either "success" or "error". 
    If it's "success" then the other fields will hold actual data. "error_code" will be "No Error".
    If it's "error" then all of the other fields will be 0 or "NULL" depending on if it's a string or an integer. "error_code" will be a string value that describes the error.

/api/Courses:
    {
        "status": string,
        "error_code":string,
        "Course_ID": integer,
        "Course_Name": string,
        "Course_Number_Credits": integer,
        "Course_Rubric": string,
        "Course_Number": integer
    }

/api/Sections:
    {
        "status": string,
        "error_code":string,
        "Section_ID": integer,
        "Section_Semester": string,
        "Section_Course_ID": integer,
        "Section_Schedule": string,
        "Section_Instructor": string
    }

/api/Students:
    {
        "status": string,
        "error_code":string,
        "Student_ID": integer,
        "Student_Name": string,
        "Student_Address": string,
        "Student_Email": string
    }

/api/Registrations:
    {
        "status": string,
        "error_code":string,
        "Student_ID": integer,
        "Registration_SectionID": integer,
        "Registration_StudentID": integer,
        "Registration_Grade": string
    }
'''


@app.route('/api/Courses', methods=['GET'])
def search_course():
    pass

@app.route('/api/Courses', methods=['DELETE'])
def delete_course():
    pass

@app.route('/api/Courses', methods=['PATCH'])
def modify_course():
    pass

@app.route('/api/Courses', methods=['POST'])
def add_course():
    pass

@app.route('/api/Sections', methods=['GET'])
def search_section():
    pass

@app.route('/api/Sections', methods=['DELETE'])
def delete_section():
    pass

@app.route('/api/Sections', methods=['PATCH'])
def modify_section():
    pass

@app.route('/api/Sections', methods=['POST'])
def add_section():
    pass

@app.route('/api/Students', methods=['GET'])
def search_student():
    pass

@app.route('/api/Students', methods=['DELETE'])
def delete_student():
    pass

@app.route('/api/Students', methods=['PATCH'])
def modify_student():
    pass

@app.route('/api/Students', methods=['POST'])
def add_student():
    pass

@app.route('/api/Registrations', methods=['GET'])
def search_registration():
    pass

@app.route('/api/Registrations', methods=['DELETE'])
def delete_registration():
    pass

@app.route('/api/Registrations', methods=['PATCH'])
def modify_registration():
    pass

@app.route('/api/Registrations', methods=['POST'])
def add_registration():
    pass


# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
