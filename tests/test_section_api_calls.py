import unittest, json, sys, os, urllib.parse
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import app

DATABASE = './db/registration_system.db'
INIT_SCRIPT = './db/script.sql'

@patch('app.DATABASE', new=DATABASE)
@patch('app.INIT_SCRIPT', new=INIT_SCRIPT)
class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_post_section(self):
        refresh_fake_database()
        section = {"Section_Semester": "Fall",
                  "Section_Course_ID": 54,
                  "Section_Schedule": "Mondays 0800",
                  "Section_Instructor": "Professor person"
                 }

        response = self.app.post('/api/Sections', data=json.dumps(section), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")
        self.assertIn("error_code", data)
        self.assertEqual(data["error_code"], "No_Error")
        self.assertIn("Section_ID", data)

        self.assertIn("Section_Semester", data)
        self.assertEqual(data["Section_Semester"], "Fall")
        self.assertIn("Section_Course_ID", data)
        self.assertEqual(data["Section_Course_ID"], 54)
        self.assertIn("Section_Schedule", data)
        self.assertEqual(data["Section_Schedule"], "Mondays 0800")
        self.assertIn("Section_Instructor", data)
        self.assertEqual(data["Section_Instructor"], "Professor person")

    def test_get_section(self):
        refresh_fake_database()
        section = {"Section_ID": 1,
                   "Section_Semester": "Fall",
                   "Section_Course_ID": 54,
                   "Section_Schedule": "Mondays 0800",
                   "Section_Instructor": "Professor person"
                  }

        response = self.app.post('/api/Sections', data=json.dumps(section), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        fetch_string = '/api/Sections?' + urllib.parse.urlencode(section)

        response = self.app.get(fetch_string, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")
        self.assertIn("error_code", data)
        self.assertEqual(data["error_code"], "No_Error")
        self.assertIn("Section_ID", data)

        self.assertIn("Section_Semester", data)
        self.assertEqual(data["Section_Semester"], "Fall")
        self.assertIn("Section_Course_ID", data)
        self.assertEqual(data["Section_Course_ID"], 54)
        self.assertIn("Section_Schedule", data)
        self.assertEqual(data["Section_Schedule"], "Mondays 0800")
        self.assertIn("Section_Instructor", data)
        self.assertEqual(data["Section_Instructor"], "Professor person")

    def test_get_all_section(self):
        refresh_fake_database()
        for i in range(50):
            section_1 = {"Section_Semester": f"Semester {i}",
                         "Section_Course_ID": 54,
                         "Section_Schedule": "Mondays 0800",
                         "Section_Instructor": "Professor person"
                        }
            response = self.app.post('/api/Sections', data=json.dumps(section_1), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            section_2 = {"Section_Semester": f"Semester {i}",
                         "Section_Course_ID": 73,
                         "Section_Schedule": "Mondays 0800",
                         "Section_Instructor": "Professor person"
                        }
            response = self.app.post('/api/Sections', data=json.dumps(section_2), content_type='application/json')
            self.assertEqual(response.status_code, 200)

        query = {"Section_ID": "ALL",
                 "Section_Semester": "NULL",
                 "Section_Course_ID": 54,
                 "Section_Schedule": "NULL",
                 "Section_Instructor": "NULL"
                }

        fetch_string = '/api/Sections?' + urllib.parse.urlencode(query)

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