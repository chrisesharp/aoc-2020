import unittest
from game import Game, get_cells

class GameTest(unittest.TestCase):
    def test_single_cell_in_world_dies(self):
        game = Game([(0,0,0)])
        self.assertTrue(game.is_alive((0,0,0)))
        game.generate()
        self.assertFalse(game.is_alive((0,0,0)))
    
    def test_stable_block_survives(self):
        data = """.#.
..#
###"""
        game = Game(get_cells(data.splitlines()))
        game.generate()
        self.assertEqual(11, len(game.alive))
        game.generate()
        self.assertEqual(21, len(game.alive))
        game.generate()
        game.generate()
        game.generate()
        game.generate()
        self.assertEqual(112, len(game.alive))
    
    def test_pt2(self):
        data = """.#.
..#
###"""
        game = Game(get_cells(data.splitlines(),True))
        game.generate()
        self.assertEqual(29, len(game.alive))
        # game.generate()
        # game.generate()
        # game.generate()
        # game.generate()
        # game.generate()
        # self.assertEqual(848, len(game.alive))

if __name__ == '__main__':
    unittest.main()