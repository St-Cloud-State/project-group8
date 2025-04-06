from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE = './db/registration_system.db'
INIT_SCRIPT = './db/script.sql'

HTML_INDEX = 'index.html'

'''
    API Calls will always return a json with these key/value pairs. The values will represent the state of the database
        after the command has been completed. The only Exception will be "DELETE" calls which will only contain the primary
        ID key, all the other values will be 0 or "NULL"

    The "status" field will always be either "success" or "error". 
        If it's "success" then the other fields will hold actual data. "error_code" will be "No Error".
        If it's "error" then all of the other fields will be 0 or "NULL" depending on if it's a string or an integer. 
            "error_code" will be a string value that describes the error.

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
    try:
        # Connect to the DB.
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get data from API Call.
        data = request.get_json()
        name    = data.get("Course_Name")
        credits = data.get("Course_Number_Credits")
        rubric  = data.get("Course_Rubric")
        number  = data.get("Course_Number")

        # Insert that data.
        cursor.execute(f"INSERT INTO Courses (course_id, course_name, course_number_credits, course_rubric, course_number) "
                       f"VALUES (NULL, '{name}', '{credits}', '{rubric}', '{number}')"
                       )

        # Get the id the sql created.
        id = cursor.lastrowid

        # Fetch the data to verify that it was added
        cursor.execute(f"SELECT * FROM Courses WHERE course_id = '{id}'")
        row = cursor.fetchone()

        ret = {"status"                 : "error",
               "error_code"             : "No_Error",
               "Course_ID"              : row["Course_ID"],
               "Course_Name"            : row["Course_Name"],
               "Course_Number_Credits"  : row["Course_Number_Credits"],
               "Course_Rubric"          : row["Course_Rubric"],
               "Course_Number"          : row["Course_Number"]
              }

        # Commit all the changes
        conn.commit()
    except Exception as e:
        ret = {"status": "error",
               "error_code":str(e),
               "Course_ID": 0,
               "Course_Name": "NULL",
               "Course_Number_Credits": 0,
               "Course_Rubric": "NULL",
               "Course_Number": 0
              }

    finally:
        conn.close()
        return jsonify(ret)

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
    return render_template(HTML_INDEX)

def prep_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    with open(INIT_SCRIPT, 'r') as file:
        sql_script = file.read()

    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    prep_db()
    app.run(debug=True, host="0.0.0.0")
