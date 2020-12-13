def get_wait(notes):
    earliest = int(notes[0])
    buses = list(map(int,notes[1].replace('x,','').split(',')))
    for time in range(earliest,earliest*10):
        for bus in buses:
            if time % bus == 0:
                return (time - earliest) * bus

def get_earliest(notes):
    constraints = [int(bus) if bus != "x" else False for bus in notes[1].split(",")]
    bus_times = {constraint: -i % constraint for i, constraint in enumerate(constraints) if constraint}
    buses = list(sorted(bus_times))
    slowest = buses.pop()
    time = bus_times[slowest]
    while buses:
        bus = buses.pop()
        while time % bus != bus_times[bus]:
            time += slowest
        slowest *= bus
    return time

if __name__ == '__main__':
    notes = open("input.txt", "r").readlines()
    print("Part 1:",get_wait(notes))
    print("Part 2:",get_earliest(notes))