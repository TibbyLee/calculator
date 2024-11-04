import unittest
from calculator import Calculator
    
class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(1, 2)

    
    def test_calculator(self):
        self.assertTrue(self.cal.calculator())

if __name__ == '__main__': #標準寫法，主程式
    unittest.main()
