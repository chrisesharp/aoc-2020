import unittest
from decode import decode, decode_row, decode_column

class GameTest(unittest.TestCase):
    def test_check_fields(self):
        code = "FBFBBFFRLR"
        self.assertEqual(44, decode_row(code))
        self.assertEqual(5, decode_column(code))
        self.assertEqual(357, decode(code))
    
    def test_check_fields_2(self):
        code = "BFFFBBFRRR"
        self.assertEqual(70, decode_row(code))
        self.assertEqual(7, decode_column(code))
        self.assertEqual(567, decode(code))
    
    def test_check_fields_3(self):
        code = "FFFBBBFRRR"
        self.assertEqual(14, decode_row(code))
        self.assertEqual(7, decode_column(code))
        self.assertEqual(119, decode(code))
    
    def test_check_fields_4(self):
        code = "BBFFBBFRLL"
        self.assertEqual(102, decode_row(code))
        self.assertEqual(4, decode_column(code))
        self.assertEqual(820, decode(code))


if __name__ == '__main__':
    unittest.main()
