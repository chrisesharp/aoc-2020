import unittest
from xmas import find_pair, find_invalid, find_contiguous, find_weakness

class GameTest(unittest.TestCase):
    def test_find_combination(self):
        data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
        stream = data.splitlines()
        self.assertTrue(find_pair(5, stream[:6]))

    def test_find_combination_looped(self):
        data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
        stream = data.splitlines()
        invalid = find_invalid(5, stream)
        self.assertEqual(127, invalid)
    
    def test_find_combination_contiguous(self):
        data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
        stream = data.splitlines()
        invalid = find_invalid(5, stream)
        group = find_contiguous(invalid, stream)
        weakness = min(group) + max(group)
        self.assertEqual(62, weakness)
    
    def test_answers(self):
        data = open("input.txt","r").readlines()
        invalid = find_invalid(25, data)
        self.assertEqual(31161678, invalid)
        self.assertEqual(5453868, find_weakness(invalid, data))
        
if __name__ == '__main__':
    unittest.main()
