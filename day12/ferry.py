from enum import Enum

class Dir(Enum):
    E = 0
    S = 1
    W = 2
    N = 3

    def delta(self):
        translations = { Dir.E: (+1,0), Dir.S: (0,+1), Dir.W: (-1,0), Dir.N: (0,-1)}
        return translations[self]

    def turns(self, turn):
        return Dir((self.value + turn + 4)%4)

class Turn(Enum):
    R = 1
    F = 0
    L = -1

    def rotation(self, size):
        return self.value * int(size / 90)

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def translate(orig, delta, dist):
    (dx,dy) = delta
    (x,y) = orig
    return (x + (dx * dist), y + (dy * dist))

class Ferry:
    def __init__(self, instructions):
        self.instructions = instructions
        self.dir = Dir.E
        self.pos = self.orig = (0,0)

    def move(self):
        instruction = self.instructions.pop(0)
        letter = instruction[0]
        size = int(instruction[1:])
        if letter in ['L','R','F']:
            self.turn(Turn[letter], size)
        else:
            self.translate(Dir[letter], size)
        return self.pos, self.dir
    
    def turn(self, turn, size):
        if turn.value:
            self.turn_ship(turn, size)
        else:
            self.move_ship(self.dir.delta(),size)
    
    def translate(self, direction, size):
        self.pos = translate(self.pos, direction.delta(), size)

    def turn_ship(self, turn, size):
        self.dir = self.dir.turns(turn.rotation(size))
    
    def move_ship(self, delta, size):
        self.pos = translate(self.pos, delta, size)

    def travel(self):
        while self.instructions:
            self.move()
        return distance(self.orig, self.pos)

class Ferry2(Ferry):
    def __init__(self, instructions):
        Ferry.__init__(self, instructions)
        self.waypoint = (10,-1)
    
    def turn(self, turn, size):
        if turn.value:
            self.turn_waypoint(turn, size)
        else:
            self.move_ship(self.waypoint, size)
    
    def turn_waypoint(self, turn, size):
        x, y = self.waypoint
        turn = turn.rotation(size)
        for i in range(abs(turn)):
            (x,y) = (-y,x) if turn > 0 else (y, -x)
        self.waypoint = (x,y)
    
    def translate(self, direction, size):
        self.waypoint = translate(self.waypoint, direction.delta(), size)


if __name__ == '__main__':
    instructions = open("input.txt","r").readlines()
    ship1 = Ferry(instructions[:])
    print("Part 1:", ship1.travel())

    ship2 = Ferry2(instructions[:])
    print("Part 2:",ship2.travel())