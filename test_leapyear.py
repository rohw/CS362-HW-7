import unittest
import leapyear


class SimpleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.ly(4), "It is a leap year")

    def test2(self):
        self.assertEqual(leapyear.ly(100), "It is not a leap year")


if __name__ == '__main__':
    unittest.main()
