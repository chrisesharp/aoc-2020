from enum import Enum

class Dir(Enum):
    E = 0
    S = 1
    W = 2
    N = 3

class Turn(Enum):
    R = 1
    F = 0
    L = -1

translations = {
    Dir.E: (+1,0),
    Dir.S: (0,+1),
    Dir.W: (-1,0),
    Dir.N: (0,-1)
}

def rotation(turn, size):
    return turn.value * int(size / 90)

def distance(a, b):
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2) + abs(y1-y2)

def translate(orig, direction, dist):
    (dx,dy) = direction
    (x,y) = orig
    x += dx * dist
    y += dy * dist
    return (x,y)

class Ferry:
    def __init__(self, instructions, part2=False):
        self.instructions = instructions
        self.waypoint = (10,-1)
        self.dir = Dir.E
        self.pos = self.orig = (0,0)
        self.part2 = part2

    def move(self):
        instruction = self.instructions.pop(0)
        letter = instruction[0]
        size = int(instruction[1:])
        if letter in ['L','R','F']:
            turn = Turn[letter]
            if self.part2:
                if turn.value:
                    self.turn_waypoint(turn, size)
                else:
                    self.move_ship(self.waypoint,size)
            else:
                if turn.value:
                    self.turn_ship(turn, size)
                else:
                    self.move_ship(translations[self.dir],size)
        else:
            direction = Dir[letter]
            if self.part2:
                self.waypoint = translate(self.waypoint, translations[direction], size)
            else:
                self.pos = translate(self.pos, translations[direction], size)
        return self.pos, self.dir

    def turn_ship(self, turn, size):
        turn = rotation(turn, size)
        self.dir = Dir((self.dir.value + turn + 4)%4)
    
    def turn_waypoint(self, turn, size):
        x, y = self.waypoint
        turn = rotation(turn, size)
        for i in range(abs(turn)):
            (x,y) = (-y,x) if turn > 0 else (y, -x)
        self.waypoint = (x,y)
    
    def move_ship(self, delta, size):
        self.pos = translate(self.pos, delta, size)

    def travel(self):
        while self.instructions:
            self.move()
        return distance(self.orig, self.pos)

if __name__ == '__main__':
    instructions = open("input.txt","r").readlines()
    ship1 = Ferry(instructions[:])
    print("Part 1:", ship1.travel())

    ship2 = Ferry(instructions[:],True)
    print("Part 2:",ship2.travel())