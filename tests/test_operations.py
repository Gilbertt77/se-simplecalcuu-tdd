import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    ##def test_subtract(self):
        # TODO: add assertions for subtract
       # self.assertEqual(subtract(5,2), 3)
        #self.assertEqual(subtract(10,3), 7)
        #self.assertEqual(subtract(50,4), 46)
        #pass

    #def test_multiply(self):
        # TODO: add assertions for multiply
        #self.assertEqual(multiply(20,3), 60)
        #self.assertEqual(multiply(4,3), 12)
        #self.assertEqual(multiply(5,4), 20)
        #pass

    #def test_divide(self):
        # TODO: add assertions for divide
        #self.assertEqual(divide(10,2), 5)
        #self.assertEqual(divide(80,2), 40)
        #self.assertEqual(divide(10,5), 2)
        #pass
    ##
if __name__ == '__main__':
    unittest.main()
