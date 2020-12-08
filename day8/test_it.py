import unittest
from cpu import CPU

class GameTest(unittest.TestCase):
    def test_parse_rules(self):
        data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(data.splitlines())
        cpu.next()
        cpu.next()
        self.assertEqual(1, cpu.acc)
        self.assertEqual(2, cpu.pc)
    
    def test_detect_loop(self):
        data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(data.splitlines())
        while cpu.next():
            pass
        self.assertEqual(5, cpu.acc)
        
if __name__ == '__main__':
    unittest.main()
