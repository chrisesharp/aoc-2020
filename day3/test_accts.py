import unittest

class GameTest(unittest.TestCase):
    def test_find_1721_299(self):
        input = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(2020, sum(pair))

if __name__ == '__main__':
    unittest.main()
