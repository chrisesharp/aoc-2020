import unittest
from ferry import Ferry, Dir

class GameTest(unittest.TestCase):
    def test_move(self):
        data = """F10
N3
F7
R90
F11"""
        instructions = data.splitlines()
        ferry = Ferry(instructions)
        (pos, facing) = ferry.move()
        self.assertEqual((10,0), pos)
        self.assertEqual(Dir.E, facing)
        (pos, facing) = ferry.move()
        self.assertEqual((10,-3), pos)
        self.assertEqual(Dir.E, facing)
    
    def test_travel(self):
        data = """F10
N3
F7
R90
F11"""
        instructions = data.splitlines()
        ferry = Ferry(instructions)
        distance = ferry.travel()
        self.assertEqual(25, distance)
        
if __name__ == '__main__':
    unittest.main()
