import unittest
import jolts

class GameTest(unittest.TestCase):
    def test_find_(self):
        data = """16
10
15
5
1
11
7
19
6
12
4"""
        adapters = list(sorted(map(int, data.splitlines())))
        diffs = jolts.find_diffs(adapters)
        self.assertEqual((7,5), diffs)
    
    def test_perm_1(self):
        data = """16
10
15
5
1
11
7
19
6
12
4"""
        adapters = list(sorted(map(int, data.splitlines())))
        perms = jolts.find_perms(adapters)
        self.assertEqual(8, perms)

    def test_perm_2(self):
        data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
        adapters = list(sorted(map(int, data.splitlines())))
        perms = jolts.find_perms(adapters)
        self.assertEqual(19208, perms)
        
if __name__ == '__main__':
    unittest.main()
