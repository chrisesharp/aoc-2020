import unittest
from encrypt import transform, private

class GameTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5764801, transform(7,8))
        self.assertEqual(8, private(5764801))
        self.assertEqual(17807724, transform(7,11))
        self.assertEqual(11, private(17807724))
        self.assertEqual(14897079, transform(17807724,8))
        self.assertEqual(14897079, transform(5764801,11))

if __name__ == '__main__':
    unittest.main()
