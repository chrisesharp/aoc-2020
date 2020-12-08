def decode(instruction):
    return instruction.split(' ',1)

class CPU:
    def __init__(self, code = []):
        self.mem = self.load(code)
        self.reset()
    
    def reset(self):
        self.pc = 0
        self.acc = 0
        for i in range(self.end):
            self.mem[i]['dirty'] = False
    
    def load(self, code):
        mem = {}
        for i in range(len(code)):
            (op, parms) = decode(code[i])
            mem[i] = {"op":op,"parms":parms}
        self.end = i
        return mem
    
    def next(self):
        if self.pc == self.end:
            return False
        if instruction := self.mem.get(self.pc, False):
            return self.execute(instruction)
        return False

    def execute(self, instruction):
        (op, parm, dirty) = instruction.values()
        if dirty:
            return False
        self.mem[self.pc]['dirty']=True
        if op == "acc":
            self.acc += int(parm)
            self.pc += 1
        elif op == "jmp":
            self.pc += int(parm)
        else:
            self.pc += 1
        return True
    
    def run(self):
        while self.next(): pass
        return self.acc

    def run_with_mod(self):
        for i in range(self.end):
            if self.mem[i]['op'] != 'jmp':
                continue
            self.mem[i]['op'] = "nop"
            while self.next():
                if self.pc == self.end:
                    return self.acc
            self.mem[i]['op'] = "jmp"
            self.reset()

if __name__ == '__main__':
    data = open("input.txt","r").readlines()
    cpu = CPU(data)
    print("Part 1:",cpu.run())
    cpu.reset()
    print("Part 2:",cpu.run_with_mod())
