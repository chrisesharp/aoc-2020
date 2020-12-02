import unittest
import passwords

class GameTest(unittest.TestCase):
    def test_validate_record(self):
        input_rec = "1-3 a: abcde"
        self.assertTrue(passwords.is_valid1(input_rec))
    
    def test_validate_file(self):
        records = open("test.txt", "r").readlines()
        counter = 0
        for record in records:
            counter += passwords.is_valid1(record.strip()) 
        self.assertEqual(2, counter)
    
    def test_validate_record_v2(self):
        input_rec = "1-3 a: abcde"
        self.assertTrue(passwords.is_valid2(input_rec))
    
    def test_validate_file_v2(self):
        records = open("test.txt", "r").readlines()
        counter = 0
        for record in records:
            counter += passwords.is_valid2(record.strip()) 
        self.assertEqual(1, counter)


if __name__ == '__main__':
    unittest.main()