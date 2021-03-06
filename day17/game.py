import itertools

def permutations(iterable):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.product(range(-1,2), repeat=n):
        if indices.count(0) != n:
            sum_list = ([a + b for a, b in zip(pool, indices)])
            yield tuple(sum_list)

def get_cells(data, pt2=False):
    cells = []
    width = len(data[0].strip())
    height = len(data)
    for y in range(width):
        for x in range(height):
            if data[y][x] == '#':
                cell = (x,y,0) if not pt2 else (x,y,0,0)
                cells.append(cell) 
    return cells

class Game():
    def __init__(self, initial_state):
        self.alive = set(initial_state)

    def generate(self):        
        self.alive = self.survivors() | self.births()
    
    def survivors(self):
        survivors = set()
        for cell in self.alive:
            if self.will_survive(cell):
                survivors.add(cell)
        return survivors
    
    def births(self):
        births = set()
        for cell in self.alive:
            for neighbour in self.neighbours(cell):
                if self.will_birth(neighbour):
                    births.add(neighbour)
        return births

    def will_survive(self, cell):
        live_neighbours = self.live_neighbour_count(cell)
        return (live_neighbours == 2) or (live_neighbours == 3)
    
    def will_birth(self, cell):
        live_neighbours = self.live_neighbour_count(cell)
        return (live_neighbours == 3)
    
    def live_neighbour_count(self, cell):
        return len(self.alive & self.neighbours(cell))
    
    def neighbours(self, cell):
        return set(permutations(cell))

    def is_alive(self, cell):
        return cell in self.alive

if __name__ == '__main__':
    cells = get_cells(open("input.txt","r").readlines())
    game = Game(cells)
    for i in range(6):
        game.generate()
    print("Part 1",len(game.alive))
    cells = get_cells(open("input.txt","r").readlines(), True)
    game = Game(cells)
    for i in range(6):
        game.generate()
    print("Part 2",len(game.alive))

