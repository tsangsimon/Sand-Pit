import app
import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    #Nothing to put into the teardown for this testcase
    #def tearDown(self):

    def test_hello_world(self):
        rv = self.app.get('/')
        assert 'Hello World' in rv.data

if __name__ == '__main__':
    unittest.main()
