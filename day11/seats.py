def sign(a,b):
    return 0 if a==b else (-1 if (a < b) else 1)

def get_delta(origin, target):
    return (sign(target[0],origin[0]),sign(target[1],origin[1]))

class Seats:
    def __init__(self, layout):
        self.layout = {}
        self.width = len(layout[0].strip())
        self.height = len(layout)
        for x,y in [(x,y) for x in range(self.width) for y in range(self.height) if layout[y][x] in ['L','#']]:
            self.layout[(x,y)] = layout[y][x]

    def apply_rules(self, seat, part2=False):
        occupied = (self.layout[seat] == '#')
        neighbours = self.neighbours(seat, part2)
        if not occupied and neighbours == 0:
            return '#'
        elif neighbours >= (4 + int(part2)):
            return "L"
        return self.layout[seat]

    def neighbours(self, origin, part2=False):
        x,y = origin
        count = 0
        seats = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
        visited = []
        while seats:
            seat = seats.pop()
            visited.append(seat)
            if seat in self.layout:
                count += (self.layout.get(seat,".") == "#")
            elif part2:
                delta = get_delta(origin, seat)
                next_seat = self.find_next_seat(seat, delta)
                if next_seat and next_seat not in visited:
                    seats.append(next_seat)
        return count

    def find_next_seat(self, seat, delta):
        x, y = seat
        dx, dy = delta
        while (x >= 0 and x < self.width and y >= 0 and y < self.height):
            x += dx
            y += dy
            if (x,y) in self.layout:
                return (x,y)
        return False

    def next(self, part2=False):
        new_layout = {}
        for seat in self.layout:
            new_layout[seat] = self.apply_rules(seat, part2) 
        self.layout = new_layout
    
    def occupied(self):
        return list(self.layout.values()).count('#')

if __name__ == '__main__':
    data = open("input.txt","r").readlines()
    layout = Seats(data)
    layout.next()
    prev = 0
    current = layout.occupied()
    while current != prev:
        prev = current
        layout.next()
        current = layout.occupied()
    print("Part 1:",current)
    layout = Seats(data)
    layout.next()
    prev = 0
    current = layout.occupied()
    while current != prev:
        prev = current
        layout.next(True)
        current = layout.occupied()
    print("Part 2:",current)

