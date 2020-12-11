import unittest
from seats import Seats

class GameTest(unittest.TestCase):
    def test_count(self):
        data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
        layout = data.splitlines()
        layout = Seats(layout)
        for i in range(5):
            layout.next()
        self.assertEqual(37,layout.occupied())

    def test_new_rules(self):
        data = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
        layout = data.splitlines()
        layout = Seats(layout)
        self.assertEqual('L', layout.layout[3,4])
        self.assertEqual(8, layout.neighbours((3,4),True))
    
if __name__ == '__main__':
    unittest.main()
