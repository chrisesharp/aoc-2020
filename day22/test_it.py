import unittest
from cards import Cards, RecursiveCombat

class GameTest(unittest.TestCase):
    def test_1(self):
        data = open("test.txt","r").read().split("\n\n")
        game = Cards()
        game.deal(data)
        game.play()
        self.assertEqual([3, 2, 10, 6, 8, 5, 9, 4, 7, 1], game.winner)
        self.assertEqual(306, game.score())
    
    def test_2(self):
        data = open("test.txt","r").read().split("\n\n")
        game = RecursiveCombat()
        game.deal(data)
        game.play()
        self.assertEqual([7, 5, 6, 2, 4, 1, 10, 8, 9, 3],game.winner)
        self.assertEqual(291, game.score())

if __name__ == '__main__':
    unittest.main()