def is_valid1(record):
    (minimum, maximum), letter, password = get_fields(record)
    return (minimum <= password.count(letter) <= maximum)

def is_valid2(record):
    (one, two), letter, password = get_fields(record)
    first = password[one - 1] == letter
    second = password[two - 1] == letter
    return (first != second and (first or second))

def get_fields(record):
    policy, password = record.split(":")
    password = password.lstrip().strip()
    occurs, letter = policy.split(" ")
    return list(map(int,occurs.split("-"))), letter, password


if __name__ == '__main__':
    records = open("input.txt", "r").readlines()
    part1 = part2 = 0
    for record in records:
        part1 += is_valid1(record)
        part2 += is_valid2(record)
    print("Part 1:",part1)
    print("Part 2:",part2)