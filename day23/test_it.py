import unittest
from cups import Cups

def move(cups):
    pass

class GameTest(unittest.TestCase):
    def test_pt1(self):
        data = "389125467"
        game = Cups(data)
        self.assertEqual("67384529", game.play())
    
    def test_pt2(self):
        data = "389125467"
        game = Cups(data)
        self.assertEqual(149245887792, game.play(True))
    
if __name__ == '__main__':
    unittest.main()
