def decode_part(code, digits):
    return int('0b' + code.translate(str.maketrans(digits,"01")), 2)

def decode_row(code):
    return decode_part(code[:7], "FB")

def decode_column(code):
    return decode_part(code[-3:], "LR")

def decode(code):
    return (decode_row(code) * 8) + decode_column(code)

if __name__ == '__main__':
    highest = 0
    seats = set()
    for code in open("input.txt", "r").readlines():
        seat_id = decode(code[:10])
        seats.add(seat_id)
        highest = max(highest, seat_id)
    print("Part1:", highest)

    for seat in range(1024):
        if seat not in seats and seat-1 in seats and seat+1 in seats:
            print("Part2:",seat)
            break