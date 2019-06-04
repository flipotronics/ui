 #!/usr/bin/env python
 
import unittest
import web

class Test(unittest.TestCase):

    def setUp(self):
        web.testing = True
        self.app = web.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(b'Environment variables', rv.data)


if __name__ == '__main__':
    unittest.main()
