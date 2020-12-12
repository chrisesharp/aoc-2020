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

def distance(a, b):
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2) + abs(y1-y2)

def translate(orig, direction, dist):
    (dx,dy) = translations[direction]
    (x,y) = orig
    for i in range(dist):
        x += dx
        y += dy
    return (x,y)

class Ferry:
    def __init__(self, instructions, part2=False):
        self.instructions = instructions
        self.waypoint = (10,-1)
        self.dir = Dir.E
        self.pos = self.orig = (0,0)
        self.part2 = part2

    def translate(self, origin, direction, dist):
        (dx,dy) = translations[direction]
        (x,y) = origin
        for i in range(dist):
            x += dx
            y += dy
        return (x,y)

    def move(self):
        instruction = self.instructions.pop(0)
        letter = instruction[0]
        size = int(instruction[1:])
        if letter in ['L','R','F']:
            letter = Turn[letter]
            if self.part2:
                if letter in [Turn.L, Turn.R]:
                    self.turn_waypoint(letter, size)
                else:
                    self.move_to_waypoint(size)
            else:
                if letter in [Turn.L, Turn.R]:
                    self.turn_ship(letter, size)
                else:
                    self.move_ship(size)
        else:
            letter = Dir[letter]
            if self.part2:
                self.waypoint = translate(self.waypoint, letter, size)
            else:
                self.pos = translate(self.pos, letter, size)
        return self.pos, self.dir

    def turn_ship(self, letter, size):
        turn = letter.value * int(size / 90)
        self.dir = Dir((self.dir.value + turn + 4)%4)
    
    def turn_waypoint(self, letter, size):
        x, y = self.waypoint
        turn = letter.value * int(size / 90)
        for i in range(abs(turn)):
            if turn > 0:
                (x,y) = (-y,x)
            else:
                (x,y) = (y, -x)
        self.waypoint = (x,y)
    
    def move_ship(self, size):
        self.pos = self.translate(self.pos, self.dir, size)

    def move_to_waypoint(self, size):
        dx,dy = self.waypoint
        x,y = self.pos
        for i in range(size):
            x += dx
            y += dy
        self.pos = (x,y)

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