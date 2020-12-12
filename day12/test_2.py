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
        ferry = Ferry(instructions, True)
        (pos, facing) = ferry.move()
        self.assertEqual((100,-10), pos)
        self.assertEqual(Dir.E, facing)
        (pos, facing) = ferry.move()
        self.assertEqual((100,-10), pos)
        self.assertEqual((10,-4), ferry.waypoint)
        (pos, facing) = ferry.move()
        self.assertEqual((170,-38),pos)
        (pos, facing) = ferry.move()
        self.assertEqual((4,10), ferry.waypoint)
        self.assertEqual((170,-38),pos)

        
if __name__ == '__main__':
    unittest.main()
