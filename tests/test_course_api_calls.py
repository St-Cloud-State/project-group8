import unittest, json, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_post_course(self):
        course = {"Course_Name": "Platform Based Development",
                  "Course_Number_Credits": 3,
                  "Course_Rubric": "CSCI",
                  "Course_Number": 414
                 }

        response = self.app.post('/api/Courses', data=json.dumps(course), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("status", data)
        self.assertIn("error_code", data)
        self.assertIn("Course_ID", data)

        self.assertIn("Course_Name", data)
        self.assertEqual(data["Course_Name"], "Platform Based Development")
        self.assertIn("Course_Number_Credits", data)
        self.assertEqual(data["Course_Number_Credits"], 3)
        self.assertIn("Course_Rubric", data)
        self.assertEqual(data["Course_Rubric"], "CSCI")
        self.assertIn("Course_Number", data)
        self.assertEqual(data["Course_Number"], 414)

if __name__ == '__main__':
    unittest.main()