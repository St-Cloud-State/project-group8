import unittest, json, sys, os
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

    def test_post_student(self):
        refresh_fake_database()
        student = {"Student_Name": "Sonny",
                   "Student_Address": "620 Madison St, Anoka MN, 55303",
                   "Student_Email": "Sonny.Dinnetz@gmail.com"
                  }

        response = self.app.post('/api/Students', data=json.dumps(student), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")
        self.assertIn("error_code", data)
        self.assertEqual(data["error_code"], "No_Error")
        self.assertIn("Student_ID", data)

        self.assertIn("Student_Name", data)
        self.assertEqual(data["Student_Name"], "Sonny")
        self.assertIn("Student_Address", data)
        self.assertEqual(data["Student_Address"], "620 Madison St, Anoka MN, 55303")
        self.assertIn("Student_Email", data)
        self.assertEqual(data["Student_Email"], "Sonny.Dinnetz@gmail.com")

    def test_get_student(self):
        refresh_fake_database()
        student = {"Student_ID": 1,
                   "Student_Name": "Sonny",
                   "Student_Address": "620 Madison St, Anoka MN, 55303",
                   "Student_Email": "Sonny.Dinnetz@gmail.com"
                  }

        response = self.app.post('/api/Students', data=json.dumps(student), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/api/Students', data=json.dumps(student), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")
        self.assertIn("error_code", data)
        self.assertEqual(data["error_code"], "No_Error")
        self.assertIn("Student_ID", data)
        
        self.assertIn("Student_Name", data)
        self.assertEqual(data["Student_Name"], "Sonny")
        self.assertIn("Student_Address", data)
        self.assertEqual(data["Student_Address"], "620 Madison St, Anoka MN, 55303")
        self.assertIn("Student_Email", data)
        self.assertEqual(data["Student_Email"], "Sonny.Dinnetz@gmail.com")

    def test_get_all_student(self):
        refresh_fake_database()
        for i in range(50):
            student_1 = {"Student_Name": f"Student {i}",
                         "Student_Address": "620 Madison St, Anoka MN, 55303",
                         "Student_Email": "Sonny.Dinnetz@gmail.com"
                        }
            response = self.app.post('/api/Students', data=json.dumps(student_1), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            student_2 = {"Student_Name": f"Student {i}",
                         "Student_Address": "620 Madison St, Anoka MN, 55303",
                         "Student_Email": "Joe.Johnson@gmail.com"
                        }
            response = self.app.post('/api/Students', data=json.dumps(student_2), content_type='application/json')
            self.assertEqual(response.status_code, 200)

        query = {"Student_ID": "ALL",
                 "Student_Name": "NULL",
                 "Student_Address": "NULL",
                 "Student_Email": "Sonny.Dinnetz@gmail.com"
                }

        response = self.app.get('/api/Students', data=json.dumps(query), content_type='application/json')
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