from flask import Flask, jsonify, render_template, request, send_file
import sqlite3, json, itertools, threading, time, os
app = Flask(__name__)

DATABASE = './db/registration_system.db'
INIT_SCRIPT = './db/script.sql'

HTML_INDEX = 'index.html'

FILE_NAME_INDEX = itertools.count(start=0, step=1)
TEMP_FOLDER = './temp'

TABLES = {"Courses":        ["Course_ID", "Course_Name", "Course_Number_Credits", "Course_Rubric", "Course_Number"], 
          "Sections":       ["Section_ID", "Section_Semester", "Section_Course_ID", "Section_Schedule", "Section_Instructor"], 
          "Students":       ["Student_ID", "Student_Name", "Student_Address", "Student_Email"], 
          "Registrations":  ["Registration_ID", "Registration_Section_ID", "Registration_Student_ID", "Registration_Grade"]
         }

@app.route('/api/get/<string:table>', methods=['GET'])
def generic_search(table):
    ret = {"status":"success", "error_code":"No_Error"}
    conn = sqlite3.connect(DATABASE)

    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if table in TABLES:
            keystrings = TABLES[table]
        else:
            raise Exception("Table Not Found")

        search = "SELECT * FROM " + table + " WHERE"
        params = []

        args = list(request.args)

        for key in args:
            if request.args.get(key) == 'NULL':
                param = "%"
            else:
                param = request.args.get(key)

            if key in keystrings:
                search += f" {key} LIKE ?"
                if key is not args[-1]:
                    search += " AND"
                params.append(param)

        cursor.execute(search, params)
        rows = cursor.fetchall()

        if len(rows) == 0:
            # This needs to tell the caller that they didn't find anything. Maybe status=success, error_code=0?
            pass
        if len(rows) == 1:
            for key in keystrings:
                ret[key] = rows[0][key]
        else:
            file_name = f"./temp/{next(FILE_NAME_INDEX)}.json"
            json_data = [dict(row) for row in rows]
            with open(file_name, 'w') as json_file:
                json.dump(json_data, json_file)
            ret["filename"] = file_name

        conn.commit()
    except Exception as e:
        ret = {"status": "error",
               "error_code":str(e)
              }
    finally:
        conn.close()
        return jsonify(ret)

@app.route('/api/post/<string:table>', methods=['POST'])
def generic_add(table):
    ret = {"status":"success", "error_code":"No_Error"}
    conn = sqlite3.connect(DATABASE)

    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if table in TABLES:
            keystrings = TABLES[table]
        else:
            raise Exception("Table Not Found")

        insert_string = f"INSERT INTO {table} ("
        values_string = ") VALUES ("

        keys = list(keystrings)
        data = request.get_json()

        for key in keys:
            insert_string += key

            if key is keys[0]:
                values_string += "NULL"
            else:
                values_string += f"'{data.get(key)}'"

            if key is not keys[-1]:
                insert_string += ", "
                values_string += ", "
            else:
                values_string += ")"

        # Insert that data.
        cursor.execute(insert_string + values_string)

        # Get the id the sql created.
        id = cursor.lastrowid

        # Fetch the data to verify that it was added
        cursor.execute(f"SELECT * FROM {table} WHERE {keys[0]} = '{id}'")
        row = cursor.fetchone()

        for key in keys:
            ret[key] = row[key]

        conn.commit()
    except Exception as e:
        ret = {"status": "error",
               "error_code":str(e),
              }
    finally:
        conn.close()
        return jsonify(ret)

@app.route('/api/delete/<string:table>', methods=['DELETE'])
def generic_delete(table):
    ret = {"status":"success", "error_code":"No_Error"}
    return jsonify(ret)

@app.route('/api/put/<string:table>', methods=['PUT'])
def generic_modify(table):
    ret = {"status":"success", "error_code":"No_Error"}
    return jsonify(ret)






@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get("filename")
    return send_file(filename, as_attachment=True)

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

def clear_temp_files():
    while 1:
        for filename in os.listdir(TEMP_FOLDER):
            file_path = os.path.join(TEMP_FOLDER, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        time.sleep(30)

if __name__ == '__main__':
    trashman = threading.Thread(target=clear_temp_files, daemon=True)
    trashman.start()

    prep_db(DATABASE)
    app.run(debug=True, host="0.0.0.0")
