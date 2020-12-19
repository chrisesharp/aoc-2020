import unittest
from matcher import Matcher

class GameTest(unittest.TestCase):
    def test_find_1(self):
        data = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
        matcher =  Matcher(data)
        self.assertEqual(2, matcher.matches())
    
if __name__ == '__main__':
    unittest.main()
