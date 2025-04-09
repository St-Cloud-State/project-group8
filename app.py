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

    When using the 'GET' method to search. If you want to search for all that fit a particular criteria put "ALL" as the
        ID you're searching for. This will indicate to python to do it's search based on the other parameters instead of
            by ID number. In that case it will not return the Course/Section/Student/Registration Fields in the json. It 
            will instead have a "data" field that will contain everything that it found.

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
    conn = sqlite3.connect(DATABASE)

    try:
        # Connect to the DB.
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get data from API Call.
        data = request.get_json()
        id = data.get("Course_ID")

        if id == "ALL":
            name    = data.get("Course_Name")
            credits = data.get("Course_Number_Credits")
            rubric  = data.get("Course_Rubric")
            number  = data.get("Course_Number")

            search = "SELECT * FROM Courses WHERE "
            conditions = []
            params = []

            if name != "NULL":
                conditions.append("Course_Name = ?")
                params.append(name)

            if credits != "NULL":
                conditions.append("Course_Number_Credits = ?")
                params.append(credits)

            if rubric != "NULL":
                conditions.append("Course_Rubric = ?")
                params.append(rubric)

            if number != "NULL":
                conditions.append("Course_Number = ?")
                params.append(number)

            search += " AND ".join(conditions)
            cursor.execute(search, params)
            rows = cursor.fetchall()
            ret = {"status": "success",
                   "error_code": "No_Error",
                   "data": [dict(row) for row in rows]
                  }
        else:
            # Fetch the data to verify that it was added
            cursor.execute(f"SELECT * FROM Courses WHERE course_id = '{id}'")
            row = cursor.fetchone()

            ret = {"status"                 : "success",
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

@app.route('/api/Courses', methods=['DELETE'])
def delete_course():
    pass

@app.route('/api/Courses', methods=['PATCH'])
def modify_course():
    pass

@app.route('/api/Courses', methods=['POST'])
def add_course():
    conn = sqlite3.connect(DATABASE)

    try:
        # Connect to the DB.
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

        ret = {"status"                 : "success",
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
    conn = sqlite3.connect(DATABASE)

    try:
        # Connect to the DB.
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get data from API Call.
        data = request.get_json()
        id = data.get("Section_ID")

        if id == "ALL":
            semester = data.get("Section_Semester")
            course = data.get("Section_Course_ID")
            schedule = data.get("Section_Schedule")
            instructor = data.get("Section_Instructor")

            search = "SELECT * FROM Sections WHERE "
            conditions = []
            params = []

            if semester != "NULL":
                conditions.append("Section_Semester = ?")
                params.append(semester)

            if course != "NULL":
                conditions.append("Section_Course_ID = ?")
                params.append(course)

            if schedule != "NULL":
                conditions.append("Section_Schedulec = ?")
                params.append(schedule)

            if instructor != "NULL":
                conditions.append("Section_Instructor = ?")
                params.append(instructor)

            search += " AND ".join(conditions)
            cursor.execute(search, params)
            rows = cursor.fetchall()
            ret = {"status": "success",
                   "error_code": "No_Error",
                   "data": [dict(row) for row in rows]
                  }
        else:
            # Fetch the data to verify that it was added
            cursor.execute(f"SELECT * FROM Sections WHERE Section_ID = '{id}'")
            row = cursor.fetchone()

            ret = {"status"                 : "success",
                   "error_code"             : "No_Error",
                   "Section_ID"             : row["Section_ID"],
                   "Section_Semester"       : row["Section_Semester"],
                   "Section_Course_ID"      : row["Section_Course_ID"],
                   "Section_Schedule"       : row["Section_Schedule"],
                   "Section_Instructor"     : row["Section_Instructor"]
                  }

        # Commit all the changes
        conn.commit()
    except Exception as e:
        ret = {"status": "error",
               "error_code":str(e),
               "Section_ID"             : 0,
               "Section_Semester"       : "NULL",
               "Section_Course_ID"      : 0,
               "Section_Schedule"       : "NULL",
               "Section_Instructor"     : "NULL"
              }

    finally:
        conn.close()
        return jsonify(ret)

@app.route('/api/Sections', methods=['DELETE'])
def delete_section():
    pass

@app.route('/api/Sections', methods=['PATCH'])
def modify_section():
    pass

@app.route('/api/Sections', methods=['POST'])
def add_section():
    conn = sqlite3.connect(DATABASE)

    try:
        # Connect to the DB.
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get data from API Call.
        data = request.get_json()
        semester    = data.get("Section_Semester")
        course_id   = data.get("Section_Course_ID")
        schedule    = data.get("Section_Schedule")
        instructor  = data.get("Section_Instructor")

        # Insert that data.
        cursor.execute(f"INSERT INTO Sections (Section_ID, Section_Semester, Section_Course_ID, Section_Schedule, Section_Instructor) "
                       f"VALUES (NULL, '{semester}', '{course_id}', '{schedule}', '{instructor}')"
                       )

        # Get the id the sql created.
        id = cursor.lastrowid

        # Fetch the data to verify that it was added
        cursor.execute(f"SELECT * FROM Sections WHERE Section_ID = '{id}'")
        row = cursor.fetchone()

        ret = {"status"                 : "success",
               "error_code"             : "No_Error",
               "Section_ID"             : row["Section_ID"],
               "Section_Semester"       : row["Section_Semester"],
               "Section_Course_ID"      : row["Section_Course_ID"],
               "Section_Schedule"       : row["Section_Schedule"],
               "Section_Instructor"     : row["Section_Instructor"]
              }

        # Commit all the changes
        conn.commit()
    except Exception as e:
        ret = {"status": "error",
               "error_code":str(e),
               "Section_ID"             : 0,
               "Section_Semester"       : "NULL",
               "Section_Course_ID"      : 0,
               "Section_Schedule"       : "NULL",
               "Section_Instructor"     : "NULL"
              }

    finally:
        conn.close()
        return jsonify(ret)





@app.route('/api/Students', methods=['GET'])
def search_student():
    conn = sqlite3.connect(DATABASE)

    try:
        # Connect to the DB.
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get data from API Call.
        data = request.get_json()
        id = data.get("Student_ID")

        if id == "ALL":
            name = data.get("Student_Name")
            address = data.get("Student_Address")
            email = data.get("Student_Email")

            search = "SELECT * FROM Students WHERE "
            conditions = []
            params = []

            if name != "NULL":
                conditions.append("Student_Name = ?")
                params.append(name)

            if address != "NULL":
                conditions.append("Student_Address = ?")
                params.append(address)

            if email != "NULL":
                conditions.append("Student_Email = ?")
                params.append(email)

            search += " AND ".join(conditions)
            cursor.execute(search, params)
            rows = cursor.fetchall()
            ret = {"status": "success",
                   "error_code": "No_Error",
                   "data": [dict(row) for row in rows]
                  }
        else:
            # Fetch the data to verify that it was added
            cursor.execute(f"SELECT * FROM Students WHERE Student_ID = '{id}'")
            row = cursor.fetchone()

            ret = {"status"                 : "success",
                   "error_code"             : "No_Error",
                   "Student_ID"             : row["Student_ID"],
                   "Student_Name"           : row["Student_Name"],
                   "Student_Address"        : row["Student_Address"],
                   "Student_Email"          : row["Student_Email"],
                  }

        # Commit all the changes
        conn.commit()
    except Exception as e:
        ret = {"status": "error",
               "error_code":str(e),
               "Student_ID"             : 0,
               "Student_Name"           : "NULL",
               "Student_Address"        : "NULL",
               "Student_Email"          : "NULL",
              }

    finally:
        conn.close()
        return jsonify(ret)

@app.route('/api/Students', methods=['DELETE'])
def delete_student():
    pass

@app.route('/api/Students', methods=['PATCH'])
def modify_student():
    pass

@app.route('/api/Students', methods=['POST'])
def add_student():
    conn = sqlite3.connect(DATABASE)

    try:
        # Connect to the DB.
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get data from API Call.
        data = request.get_json()
        name    = data.get("Student_Name")
        address   = data.get("Student_Address")
        email    = data.get("Student_Email")

        # Insert that data.
        cursor.execute(f"INSERT INTO Students (Student_ID, Student_Name, Student_Address, Student_Email) "
                       f"VALUES (NULL, '{name}', '{address}', '{email}')"
                       )

        # Get the id the sql created.
        id = cursor.lastrowid

        # Fetch the data to verify that it was added
        cursor.execute(f"SELECT * FROM Students WHERE Student_ID = '{id}'")
        row = cursor.fetchone()

        ret = {"status"                 : "success",
               "error_code"             : "No_Error",
               "Student_ID"             : row["Student_ID"],
               "Student_Name"           : row["Student_Name"],
               "Student_Address"        : row["Student_Address"],
               "Student_Email"          : row["Student_Email"],
              }

        # Commit all the changes
        conn.commit()
    except Exception as e:
        ret = {"status": "error",
               "error_code":str(e),
               "Student_ID"             : 0,
               "Student_Name"           : "NULL",
               "Student_Address"        : "NULL",
               "Student_Email"          : "NULL",
              }

    finally:
        conn.close()
        return jsonify(ret)





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

def prep_db(database):
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row

    with open(INIT_SCRIPT, 'r') as file:
        sql_script = file.read()

    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    prep_db(DATABASE)
    app.run(debug=True, host="0.0.0.0")
