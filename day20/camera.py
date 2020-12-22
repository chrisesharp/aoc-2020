import math
from collections import defaultdict
from functools import reduce
from operator import mul

class Image:
    def __init__(self, data):
        self.id = int(data[0][5:9])
        self.image = self.flip(data[1:])
    
    def flip(self, pixels):
        return tuple(reversed(pixels))
    
    def all_edges(self):
        edges = self.edges()
        return edges + [''.join(reversed(x)) for x in edges]
    
    def top_edge(self):
        return self.image[0]
    
    def bottom_edge(self):
        return self.image[-1]
    
    def left_edge(self):
        return ''.join(row[0] for row in self.image)

    def right_edge(self):
        return ''.join(row[-1] for row in self.image)

    def edges(self):
        return [self.top_edge(), self.bottom_edge(), self.left_edge(), self.right_edge()]
    
    def rotate(self):
        pixels = []
        for i in range(len(self.image)):
            s = ''.join(row[i] for row in self.image)
            pixels.append(s)
        self.image = tuple(reversed(pixels))
        return self.image
    
    def permutations(self):
        for _ in range(4):
            yield self.image
            yield self.flip(self.image)
            self.rotate()
    
    def stripped(self):
        return [x[1:-1] for x in self.image[1:-1]]

class Camera:
    def __init__(self, data):
        data = [line.strip().split('\n') for line in data]
        self.images = {}
        for pixels in data:
            img = Image(pixels)
            self.images[img.id] = img
        self.edge_map = self.find_edges()
        self.corners = self.find_corners()
    
    def find_edges(self):
        edge_map = defaultdict(list)
        for i, image in self.images.items():
            for edge in image.all_edges():
                edge_map[edge].append(i)
        return edge_map

    def find_corners(self):
        corners = []
        for n, image in self.images.items():
            cnt = 0
            for e in image.edges():
                cnt += len(self.edge_map[e]) - 1
            if cnt == 2:
                corners.append(n)
        return corners

    def pick(self, left_id, edge, get_edge):
        me = [id for id in self.edge_map[edge] if id != left_id][0]
        image = self.images[me]
        for pixels in image.permutations():
            if edge == get_edge(pixels):
                break
        image.image = pixels
        return image
    
    def assemble(self):
        image = self.images[self.corners[0]]
        while len(self.edge_map[image.left_edge()]) == 2:
            image = image.rotate()
        
        N = int(math.sqrt(len(self.images)))
        grid = [[None] * N for _ in range(N)]
        grid[0][0] = image

        for y in range(0, N):
            if y > 0:
                lgrid = grid[y-1][0]
                grid[y][0] = self.pick(lgrid.id, lgrid.bottom_edge(), get_edge=lambda x: x[0])

            for x in range(1, N):
                lgrid = grid[y][x-1]
                grid[y][x] = self.pick(lgrid.id, lgrid.right_edge(), get_edge=lambda g: ''.join(x[0] for x in g))

        composite = [[None] * N for _ in range(N)]  
        for i, row in enumerate(grid):
            for j, image in enumerate(row):
                composite[i][j] = image.stripped()
        
        data = ["Tile 9999"]
        for row in composite:
            for i in range(len(row[0])):
                data += [''.join(col[i] for col in row)]
        return Image(data)

    def find_monster(self, composite, monster):
        for image in composite.permutations():
            count = 0
            for x, y in [(x,y) for y in range(len(image)-len(monster)) for x in range(len(image)-len(monster[0]))]:
                match = True
                for dx, dy in [(dx,dy) for dy in range(len(monster)) for dx in range(len(monster[dy]))]:
                    if monster[dy][dx] == '#' and image[y + dy][x + dx] != '#':
                        match = False
                        break
                if match:
                    count += 1
            if count:
                break
        return count

if __name__ == '__main__':
    data = open("input.txt","r").read().strip().split('\n\n')
    camera = Camera(data)
    part1 = reduce(mul, camera.corners)
    print("Part 1:", part1)
    
    SEA_MONSTER = """\
                  #
#    ##    ##    ###
 #  #  #  #  #  #""".split('\n')
    composite = camera.assemble()
    count = camera.find_monster(composite, SEA_MONSTER)
    everything = ''.join(composite.image).count('#')
    monster = ''.join(SEA_MONSTER).count('#')
    print("Part 2:",everything - (monster * count))