import unittest
import math
from toboggan import *

class GameTest(unittest.TestCase):
    def test_traverse_1(self):
        map_data = open("test.txt", "r").readlines() 
        sled = Toboggan(map_data)
        sled.traverse(3,1)
        self.assertFalse(sled.hit_tree())
        sled.traverse(3,1)
        self.assertTrue(sled.hit_tree())
    
    def test_traverse_2(self):
        map_data = open("test.txt", "r").readlines() 
        sled = Toboggan(map_data)
        sled.traverse(3,1)
        sled.traverse(3,1)
        sled.traverse(3,1)
        self.assertFalse(sled.hit_tree())
    
    def test_traverse_3(self):
        map_data = open("test.txt", "r").readlines() 
        sled = Toboggan(map_data)
        sled.traverse(3,1)
        sled.traverse(3,1)
        sled.traverse(3,1)
        sled.traverse(3,1)
        self.assertTrue(sled.hit_tree())
    
    def test_run(self):
        map_data = open("test.txt", "r").readlines() 
        sled = Toboggan(map_data)
        angle = (3,1)
        hits = sled.run(angle)
        self.assertEqual(7, hits)
    
    def test_run_all(self):
        map_data = open("test.txt", "r").readlines() 
        sled = Toboggan(map_data)
        options = [(1,1),(3,1),(5,1),(7,1),(1,2)]
        hits = []
        for option in options:
            hits.append(sled.run(option))
        total = math.prod(hits)
        self.assertEqual(336, total)

    

if __name__ == '__main__':
    unittest.main()
