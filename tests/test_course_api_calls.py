import unittest, json, sys, os, urllib.parse
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import app

DATABASE = './db/fake_registration_system.db'
INIT_SCRIPT = './db/script.sql'

@patch('app.DATABASE', new=DATABASE)
@patch('app.INIT_SCRIPT', new=INIT_SCRIPT)
class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_post_course(self):
        refresh_fake_database()
        course = {"Course_Name": "Platform Based Development",
                  "Course_Number_Credits": 3,
                  "Course_Rubric": "CSCI",
                  "Course_Number": 414
                 }

        response = self.app.post('/api/Courses', data=json.dumps(course), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")
        self.assertIn("error_code", data)
        self.assertEqual(data["error_code"], "No_Error")
        self.assertIn("Course_ID", data)

        self.assertIn("Course_Name", data)
        self.assertEqual(data["Course_Name"], "Platform Based Development")
        self.assertIn("Course_Number_Credits", data)
        self.assertEqual(data["Course_Number_Credits"], 3)
        self.assertIn("Course_Rubric", data)
        self.assertEqual(data["Course_Rubric"], "CSCI")
        self.assertIn("Course_Number", data)
        self.assertEqual(data["Course_Number"], 414)

    def test_get_course(self):
        refresh_fake_database()
        course = {"Course_ID": 1,
                  "Course_Name": "Platform Based Development",
                  "Course_Number_Credits": 3,
                  "Course_Rubric": "CSCI",
                  "Course_Number": 414
                 }

        response = self.app.post('/api/Courses', data=json.dumps(course), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        fetch_string = '/api/Courses?' + urllib.parse.urlencode(course)

        response = self.app.get(fetch_string, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")
        self.assertIn("error_code", data)
        self.assertEqual(data["error_code"], "No_Error")
        self.assertIn("Course_ID", data)

        self.assertIn("Course_Name", data)
        self.assertEqual(data["Course_Name"], "Platform Based Development")
        self.assertIn("Course_Number_Credits", data)
        self.assertEqual(data["Course_Number_Credits"], 3)
        self.assertIn("Course_Rubric", data)
        self.assertEqual(data["Course_Rubric"], "CSCI")
        self.assertIn("Course_Number", data)
        self.assertEqual(data["Course_Number"], 414)

    def test_get_all_course(self):
        refresh_fake_database()
        for i in range(50):
            course_1 = {"Course_Name": f"COURSE {i}",
                        "Course_Number_Credits": 3,
                        "Course_Rubric": "CSCI",
                        "Course_Number": i
                       }
            response = self.app.post('/api/Courses', data=json.dumps(course_1), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            course_2 = {"Course_Name": f"COURSE {i}",
                        "Course_Number_Credits": 4,
                        "Course_Rubric": "CSCI",
                        "Course_Number": i
                       }
            response = self.app.post('/api/Courses', data=json.dumps(course_2), content_type='application/json')
            self.assertEqual(response.status_code, 200)

        query = {"Course_ID": "ALL",
                 "Course_Name": "NULL",
                 "Course_Number_Credits": 3,
                 "Course_Rubric": "CSCI",
                 "Course_Number": "NULL"
                }

        fetch_string = '/api/Courses?' + urllib.parse.urlencode(query)

        response = self.app.get(fetch_string, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")
        self.assertIn("error_code", data)
        self.assertEqual(data["error_code"], "No_Error")
        self.assertEqual(len(data["data"]), 50)




def refresh_fake_database():
    try:
        os.remove(DATABASE)
    except FileNotFoundError:
        pass
    except:
        raise Exception("failed to Refresh Database")
    
    app.prep_db(DATABASE)

if __name__ == '__main__':
    app.prep_db(DATABASE)
    unittest.main()