import math

def find_diffs(adapters):
    ones, threes = (0,1)
    prev = 0
    for a in adapters:
        ones += (a - prev == 1)
        threes += (a - prev == 3)
        prev = a
    return (ones, threes)

def perm_count(adapter, adapters, cache={}):
    key = (adapter,len(adapters))
    if cache.get(key, False):
        return cache[key]
    if not adapters:
        cache[key] = 1
        return 1
    
    count = 0
    while len(adapters):
        next_adapter = adapters[0]
        adapters = adapters[1:]
        if next_adapter - adapter <= 3:
            count += perm_count(next_adapter, adapters, cache)
    cache[key] = count
    return count

def find_perms(adapters):
    return perm_count(0, adapters)


if __name__ == '__main__':
    data = open("input.txt", "r").readlines()
    adapters = sorted(map(int, data))
    diffs = find_diffs(adapters)
    print("Part 1:", math.prod(diffs))
    print("Part 2:", find_perms(adapters))