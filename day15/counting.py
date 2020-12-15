class LRUCache:
    def __init__(self):
        self.cache = {}
        self.last_item = None
 
    def get(self, key: int, default=-1) -> int:
        return self.cache.get(key, default)

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.last_item = key
    
    def update(self, key: int, value: int) -> None:
        self.cache[key] = value
    
    def last(self):
        return self.last_item, self.cache[self.last_item]

def play(numbers, target):
    occurred = LRUCache()
    last_num = 0
    for i, num in enumerate(numbers):
        turn = i + 1
        occurred.put(num, [turn])
    
    while turn < target:
        turn += 1
        last_num, last_turns = occurred.last()
        if len(last_turns) == 1:
            prev = occurred.get(0)
            prev = [prev[-1], turn]
            occurred.put(0, prev)
        else:
            last_spoken = last_turns[-1]
            prev_spoken = last_turns[-2]
            next_num = last_spoken - prev_spoken
            exists = occurred.get(next_num,[])
            exists.append(turn)
            occurred.put(next_num, exists)
    return occurred.last()[0]

if __name__ == '__main__':
    data = [0,3,1,6,7,5]
    print("Part 1:", play(data, 2020))
    print("Part 2:", play(data, 30000000))