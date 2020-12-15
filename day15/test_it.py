import unittest
from counting import play

class GameTest(unittest.TestCase):
    def test_find_1(self):
        data = [0,3,6]
        self.assertEqual(436, play(data, 2020))
    
    def test_find_2(self):
        data = [0,3,1,6,7,5]
        self.assertEqual(852, play(data, 2020))
        
if __name__ == '__main__':
    unittest.main()
