padded_bin = lambda x, n: format(x, 'b').zfill(n)

def to_bin(bitmask):
    val = 0
    for bit in bitmask:
        val = (val << 1) | int(bit)
    return val

class Bitmask:
    def __init__(self,data):
        self.program = data
        self.mem = {}
    
    def execute(self):
        prog = self.program[:]
        mask = ""
        while prog:
            line = prog.pop(0).strip()
            op, val = line.split(" = ")
            if op == "mask":
                mask = val
            else:
                self.set_mem(op, val, mask)
    
    def set_mem(self, op, val, mask):
        addr = op[4:op.find("]")]
        bitmask = [0]*36
        source = padded_bin(int(val),36)
        for bit, flag in enumerate(mask):
            bitmask[bit] = int(source[bit]) if flag == 'X' else int(flag)
        self.mem[addr] = to_bin(bitmask)
    
    def sum(self):
        count = 0
        for addr in self.mem:
            count += self.mem[addr]
        return count

class Bitmask2(Bitmask):
    
    def set_mem(self, op, val, mask):
        bitmask = [0]*36
        addr = padded_bin(int(op[4:op.find("]")]),36)
        for bit, flag in enumerate(mask):
            bitmask[bit] = str(int(flag) | int(addr[bit])) if flag != 'X' else flag
        
        queue = ["".join(bitmask)]
        while queue:
            bitmask = queue.pop(0)
            x = bitmask.find('X')
            if x >= 0:
                queue.append(bitmask[:x] + '0' + bitmask[x+1:])
                queue.append(bitmask[:x] + '1' + bitmask[x+1:])
            else:
                self.mem[to_bin(bitmask)] = int(val)

if __name__ == '__main__':
    data = open("input.txt","r").readlines()
    comp = Bitmask(data)
    comp.execute()
    print("Part 1:",comp.sum())
    comp = Bitmask2(data)
    comp.execute()
    print("Part 2:",comp.sum())