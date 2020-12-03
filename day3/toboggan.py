import math

class Toboggan:
    def __init__(self, map_data):
        self.map_data = map_data
        self.width = len(self.map_data[0])
        self.length = len(self.map_data) - 1
        self.x = self.y = 0

    def traverse(self, dx, dy):
        self.x = (self.x + dx) % (self.width - 1)
        self.y += dy

    def hit_tree(self):
        return (self.map_data[self.y][self.x] == "#")
    
    def run(self, angle):
        self.x = self.y = 0
        hits = 0
        while self.y < self.length:
            self.traverse(*angle)
            hits += self.hit_tree()
        return hits

if __name__ == '__main__':
    map_data = open("input.txt", "r").readlines()
    sled = Toboggan(map_data)
    options = [(3,1),(1,1),(5,1),(7,1),(1,2)]
    hits = []
    for option in options:
        hits.append(sled.run(option))
    total = math.prod(hits)
    print("Part 1:",hits[0])
    print("Part 2:",total)