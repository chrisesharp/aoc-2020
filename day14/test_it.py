import unittest
from bitmask import Bitmask, Bitmask2

class GameTest(unittest.TestCase):
    def test_find_(self):
        data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
        comp = Bitmask(data.splitlines())
        comp.execute()
        self.assertEqual(165, comp.sum())
    
    def test_find_(self):
        data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
        comp = Bitmask2(data.splitlines())
        comp.execute()
        self.assertEqual(208, comp.sum())
    
if __name__ == '__main__':
    unittest.main()
