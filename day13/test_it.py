import unittest
from buses import get_wait, get_earliest


class GameTest(unittest.TestCase):
    def test_wait(self):
        data = """939
7,13,x,x,59,x,31,19"""
        notes = data.splitlines()
        self.assertEqual(295, get_wait(notes))
    
    def test_earliest(self):
        data = """939
7,13,x,x,59,x,31,19"""
        notes = data.splitlines()
        self.assertEqual(1068781, get_earliest(notes))
    
if __name__ == '__main__':
    unittest.main()
