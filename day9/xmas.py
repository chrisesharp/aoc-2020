def find_pair(preamble, data):
    options = list(map(int,data[:preamble]))
    target = int(data[preamble])
    for i in range(preamble):
        for j in range(i+1, len(options)):
            if options[i] + options[j] == target:
                return True

def find_invalid(preamble, data):
    i = 0
    while find_pair(preamble, data[i:i+preamble+1]): i += 1
    return int(data[i+preamble])

def find_contiguous(target, data):
    group = [int(data[0])]
    i = 1
    while i< len(data):
        total = sum(group)
        if total == target:
            return group
        if total < target:
            group.append(int(data[i]))
            i += 1
        else:
            group.pop(0)
    return [0,-1]

def find_weakness(invalid, data):
    group = find_contiguous(invalid, data)
    return min(group) + max(group)

if __name__ == '__main__':
    data = open("input.txt", "r").readlines()
    invalid = find_invalid(25, data)
    print("Part 1:", invalid)
    print("Part 2:", find_weakness(invalid, data))