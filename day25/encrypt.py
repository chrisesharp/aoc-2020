def transform(subject, loop):
    result = 1
    for _ in range(loop):
        result *= subject
        result %= 20201227
    return result

def private(pub):
    loop = 0
    priv = 1
    while (loop := loop + 1):
        priv *= 7
        priv %= 20201227
        if pub == priv:
            return loop

if __name__ == "__main__":
    keys = open("input.txt","r").readlines()
    door_pub, card_pub = list(map(int,keys))
    door_priv = private(door_pub)
    key = transform(card_pub, door_priv)
    print("Day 25: ", key)