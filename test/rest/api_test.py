import unittest
from api import app

class TestCalcAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_add(self):
        response = self.client.get('/calc/add/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 5)

    def test_subtract(self):
        response = self.client.get('/calc/subtract/5/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 3)

    def test_multiply(self):
        response = self.client.get('/calc/multiply/3/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 12)

    def test_divide_success(self):
        response = self.client.get('/calc/divide/10/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 5)

    def test_divide_fail(self):
        response = self.client.get('/calc/divide/10/0')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_power(self):
        response = self.client.get('/calc/power/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

    def test_sqrt_success(self):
        response = self.client.get('/calc/sqrt/9')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 3)

    def test_sqrt_fail(self):
        response = self.client.get('/calc/sqrt/-1')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_log10_success(self):
        response = self.client.get('/calc/log10/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 2)

    def test_log10_fail_zero(self):
        response = self.client.get('/calc/log10/0')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_log10_fail_negative(self):
        response = self.client.get('/calc/log10/-10')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()