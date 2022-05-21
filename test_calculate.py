import unittest
import calculate

class TestCalculate(unittest.TestCase):
    
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('-------------------------\n')

    def test_sum(self):
        res= calculate.sum(2,3)
        self.assertEqual(res,5)

    def test_divide(self):
        res= calculate.divide(12,4)
        self.assertEqual(res,3)

    def test_subtract(self):
        res= calculate.subtract(7,1)
        self.assertEqual(res,6)


if __name__=="__main__":
    unittest.main() 