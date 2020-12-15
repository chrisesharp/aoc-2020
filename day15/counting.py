def play(numbers, target):
    spoken = [False] * target
    for i, v in enumerate(numbers):
        spoken[int(v)] = i + 1
    last = 0
    for i in range(len(numbers) + 1, target):
        spoken[last], last = (i, 0) if not spoken[last] else (i, i - spoken[last])
    return last

if __name__ == '__main__':
    data = [0,3,1,6,7,5]
    print("Part 1:", play(data, 2020))
    print("Part 2:", play(data, 30000000))