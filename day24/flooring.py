import re

DIRS = {
        "NW": ( 0,  1, -1), "NE": ( 1,  0, -1),
     "w":  (-1,  1,  0),        "e":  ( 1, -1,  0),
        "SW": (-1,  0,  1), "SE": ( 0, -1,  1) 
}
def move(loc, dir):
    x,y,z = loc
    dx, dy, dz = DIRS[dir]
    return x+dx, y+dy, z+dz


def parse(inst):
    inst = inst.replace('ne','NE')
    inst = inst.replace('se','SE')
    inst = inst.replace('sw','SW')
    inst = inst.replace('nw','NW')
    return inst

def count_move(inst, dir):
    count = inst.count(dir)
    return count if count != -1 else 0

def simplify(inst):
    loc = (0,0,0)
    for dir in DIRS:
        for _ in range(count_move(inst, dir)):
            loc = move(loc, dir)
    return loc

class Floor:
    def __init__(self):
        self.tiles = set()
    
    def flip(self, instruction):
        instruction = parse(str(instruction))
        self.flip_tile(simplify(instruction))
    
    def flip_tile(self, tile):
        if tile in self.tiles: self.tiles.remove(tile)
        else: self.tiles.add(tile)
    
    def num_blacks(self):
        return len(self.tiles)
    
    def next_generation(self):
        blacks = set()
        for tile in self.tiles:
            if self.stay_black(tile):
                blacks.add(tile)
            for neighbour in self.neighbours(tile):
                if self.to_black(neighbour):
                    blacks.add(neighbour)
        self.tiles = blacks
    
    def stay_black(self, tile):
        black_neighbours = self.black_neighbour_count(tile)
        return (black_neighbours == 1) or (black_neighbours == 2)
    
    def to_black(self, tile):
        black_neighbours = self.black_neighbour_count(tile)
        return tile not in self.tiles and (black_neighbours == 2)
    
    def black_neighbour_count(self, tile):
        live_neighbours = 0
        for neighbour in self.neighbours(tile):
            if neighbour in self.tiles:
                live_neighbours += 1
        return live_neighbours
    
    def neighbours(self, tile):
        x, y, z = tile
        neighbours = []
        for delta in DIRS.values():
            dx, dy, dz = delta
            neighbours.append((x + dx, y + dy, z + dz))
        return neighbours

if __name__ == '__main__':
    data = open("input.txt","r").readlines()
    tiles = Floor()
    for instruction in data:
        tiles.flip(instruction)
    print("Part 1:",tiles.num_blacks())
    for _ in range(100):
        tiles.next_generation()
    print("Part 2:", tiles.num_blacks())