def find_matched_pairs(d):
    return [(i,j) for i in d for j in d if i+j == 2020]

def find_matched_triples(d):
    return [(d[i],d[j],d[k]) for i in range(len(d)) for j in range(i+1, len(d)) for k in range(j+1, len(d)) if d[i]+d[j]+d[k] == 2020]

if __name__ == '__main__':
    data = list(map(int, open("input.txt", "r").readlines()))
    pair = find_matched_pairs(data)[0]
    print("Part1:",pair[0]*pair[1])
    triple = find_matched_triples(data)[0]
    print("Part2:",triple[0]*triple[1]*triple[2])
