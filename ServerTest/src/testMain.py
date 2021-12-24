from logicGates import *
import unittest


class TestMain(unittest.TestCase):
    def test_andGate(self):
        self.assertEqual(andGate(0, 0), 0)
        self.assertEqual(andGate(0, 1), 0)
        self.assertEqual(andGate(1, 0), 0)
        self.assertEqual(andGate(1, 1), 1)
    
    def test_orGate(self):
        self.assertEqual(orGate(0, 0), 0)
        self.assertEqual(orGate(0, 1), 1)
        self.assertEqual(orGate(1, 0), 1)
        self.assertEqual(orGate(1, 1), 1)

    def test_notGate(self):
        self.assertEqual(notGate(0), 1)
        self.assertEqual(notGate(1), 0)
    
    def test_xorGate(self):
        self.assertEqual(xorGate(0, 0), 0)
        self.assertEqual(xorGate(0, 1), 1)
        self.assertEqual(xorGate(1, 0), 1)
        self.assertEqual(xorGate(1, 1), 0)

    def test_nandGate(self):
        self.assertEqual(nandGate(0, 0), 1)
        self.assertEqual(nandGate(0, 1), 1)
        self.assertEqual(nandGate(1, 0), 1)
        self.assertEqual(nandGate(1, 1), 0)


if __name__ == '__main__':
    unittest.main()