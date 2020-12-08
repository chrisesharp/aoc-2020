def decode(instruction):
    return instruction.split(' ',1)

class CPU:
    def __init__(self, code = []):
        self.mem = self.load(code)
        self.end = len(self.mem)
        self.reset()
        self.opcode = {
            "nop": self.op_nop,
            "jmp": self.op_jmp,
            "acc": self.op_acc
        }
    
    def op_nop(self, parm):
        self.pc += 1
    
    def op_jmp(self, parm):
        self.pc += int(parm)
    
    def op_acc(self, parm):
        self.acc += int(parm)
        self.pc += 1
    
    def reset(self):
        self.pc = 0
        self.acc = 0
        self.dirty = [False] * self.end
    
    def load(self, code):
        mem = {}
        for i in range(len(code)):
            (op, parms) = decode(code[i])
            mem[i] = {"op":op,"parms":parms}
        return mem
    
    def next(self):
        if self.pc != self.end and (instruction := self.mem.get(self.pc, False)):
            return self.execute(instruction)

    def execute(self, instruction):
        (op, parm) = instruction.values()
        if not self.dirty[self.pc]:
            self.dirty[self.pc] = True
            self.opcode[op](parm)
            return True
    
    def run(self):
        while self.next(): continue
        return self.acc

    def run_with_mod(self):
        for i in range(self.end):
            if self.mem[i]['op'] == 'jmp':
                if self.mutate_finishes(i,"nop"):
                    return self.acc
                self.reset()
    
    def mutate_finishes(self, location, op):
        orig = self.mem[location]['op']
        self.mem[location]['op'] = op
        self.run()
        self.mem[location]['op'] = orig
        return self.pc == self.end

if __name__ == '__main__':
    data = open("input.txt","r").readlines()
    cpu = CPU(data)
    print("Part 1:",cpu.run())
    cpu.reset()
    print("Part 2:",cpu.run_with_mod())
