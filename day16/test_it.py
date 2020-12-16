import unittest
from tickets import Scanner, get_ticket, compute_result

class GameTest(unittest.TestCase):
    def test_find_1(self):
        data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
        scanner = Scanner(data)
        self.assertEqual(71, scanner.get_error_rate())
    
    def test_find_2(self):
        data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
        scanner = Scanner(data)
        scanner.get_error_rate()
        fields = scanner.match_fields()
        expected = {
            'class':12,
            'row':11,
            'seat':13
        }
        ticket = get_ticket(scanner.your_ticket, fields)
        self.assertEqual(expected, ticket)
        self.assertEqual(1, compute_result(ticket, fields))

if __name__ == '__main__':
    unittest.main()
