import unittest
import acct

class GameTest(unittest.TestCase):
    def test_find_1721_299(self):
        input = [1721, 979, 366, 299, 675, 1456]
        pair = acct.find_matched_pairs(input)[0]
        self.assertEqual(2020, sum(pair))
    
    def test_find_979_366_675(self):
        input = [1721, 979, 366, 299, 675, 1456]
        triple = acct.find_matched_triples(input)[0]
        self.assertEqual(2020, sum(triple))

if __name__ == '__main__':
    unittest.main()