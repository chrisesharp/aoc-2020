def decode_part(code, digits):
    return int('0b' + code.replace(digits[0],'0').replace(digits[1],'1'), 2)

def decode_row(code):
    return decode_part(code[:7], ['F','B'])

def decode_column(code):
    return decode_part(code[-3:], ['L','R'])

def decode(code):
    return (decode_row(code) * 8) + decode_column(code)

if __name__ == '__main__':
    passes = open("input.txt", "r").readlines()
    highest = 0
    seats = set()
    for code in passes:
        seat_id = decode(code[:10])
        seats.add(seat_id)
        highest = max(highest, seat_id)
    print("Part1:", highest)

    for seat in range(1024):
        if seat not in seats and seat-1 in seats and seat+1 in seats:
            print("Part2:",seat)
            break