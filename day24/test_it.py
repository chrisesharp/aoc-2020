import unittest
from flooring import Floor

class GameTest(unittest.TestCase):
    def test_1(self):
        instruction = "eseneenwsw"
        tiles = Floor()
        tiles.flip(instruction)
        self.assertEqual(1, tiles.num_blacks())
        tiles.flip(instruction)
        self.assertEqual(0, tiles.num_blacks())
    
    def test_2(self):
        instruction = "nwwswee"
        tiles = Floor()
        tiles.flip(instruction)
        self.assertTrue((0,0,0) in tiles.tiles)
    
    def test_3(self):
        data = """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

        instructions = data.splitlines()
        tiles = Floor()
        for instruction in instructions:
            tiles.flip(instruction)
        self.assertEqual(10, tiles.num_blacks())
        for _ in range(100):
            tiles.next_generation()
        self.assertEqual(2208, tiles.num_blacks())
    
if __name__ == '__main__':
    unittest.main()
