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

def refresh_fake_database():
    try:
        os.remove(DATABASE)
    except FileNotFoundError:
        pass
    except:
        raise Exception("failed to Refresh Database")
    
    app.prep_db(DATABASE)

if __name__ == '__main__':
    app.prep_db()
    unittest.main()