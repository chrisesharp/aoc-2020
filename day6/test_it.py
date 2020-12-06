import unittest
import groups

class GameTest(unittest.TestCase):
    def test_check_fields(self):
        code = """abcx
abcy
abcz
"""
        self.assertEqual(6, groups.count_questions(code))
    
    def test_check_groups(self):
        code = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
        self.assertEqual(11, groups.total_yes(code))
    
    def test_check_groups_common(self):
        code = """abc"""
        self.assertEqual(3, groups.count_common(code))
    
    def test_check_total_groups(self):
        code = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
        self.assertEqual(6, groups.common_yes(code))

if __name__ == '__main__':
    unittest.main()
