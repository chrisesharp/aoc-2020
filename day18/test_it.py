import unittest
from parser import Parser, Parser2, compute

class GameTest(unittest.TestCase):
    def test_find_simple(self):
        data = "1 + 2 * 3 + 4 * 5 + 6".replace(' ','')
        parser = Parser()
        ast = parser.parse(data)
        self.assertEqual(71, compute(ast))
    
    def test_find_2(self):
        data = "1 + (2 * 3) + (4 * (5 + 6))".replace(' ','')
        parser = Parser()
        ast = parser.parse(data)
        self.assertEqual(51, compute(ast))
    
    def test_find_3(self):
        data = "2 * 3 + (4 * 5)".replace(' ','')
        parser = Parser()
        ast = parser.parse(data)
        self.assertEqual(26, compute(ast))
    
    def test_find_4(self):
        data = "5 + (8 * 3 + 9 + 3 * 4 * 3)".replace(' ','')
        parser = Parser()
        ast = parser.parse(data)
        self.assertEqual(437, compute(ast))
    
    def test_find_5(self):
        data = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))".replace(' ','')
        parser = Parser()
        ast = parser.parse(data)
        self.assertEqual(12240, compute(ast))
    
    def test_find_6(self):
        data = "1 + 2 * 3 + 4 * 5 + 6".replace(' ','')
        parser2 = Parser2()
        ast = parser2.parse(data)
        self.assertEqual(231, compute(ast))
    
    def test_find_7(self):
        data = "1 + (2 * 3) + (4 * (5 + 6))".replace(' ','')
        parser2 = Parser2()
        ast = parser2.parse(data)
        self.assertEqual(51, compute(ast))
    
    def test_find_8(self):
        data = "2 * 3 + (4 * 5)".replace(' ','')
        parser2 = Parser2()
        ast = parser2.parse(data)
        self.assertEqual(46, compute(ast))
    
    def test_find_9(self):
        data = "5 + (8 * 3 + 9 + 3 * 4 * 3)".replace(' ','')
        parser2 = Parser2()
        ast = parser2.parse(data)
        self.assertEqual(1445, compute(ast))
    
    def test_find_10(self):
        data = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))".replace(' ','')
        parser2 = Parser2()
        ast = parser2.parse(data)
        self.assertEqual(669060, compute(ast))

if __name__ == '__main__':
    unittest.main()
