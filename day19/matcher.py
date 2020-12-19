import re

class Matcher:
    def __init__(self, data):
        self.data = data
        self.rules = { int(n): r for n,r in re.findall(r'(\d+)\:(.+)\n', data.replace('"', '')) }
    
    def rr(self, n):
        new_rule = '|'.join([''.join([self.rr(int(c)) if c.isdigit() else c for c in r.split()]) for r in self.rules[n].split('|')]) 
        return new_rule if '|' not in new_rule else '(?:' + new_rule + ')'
    
    def matches(self):
        return sum(re.match('^'+self.rr(0)+'$', line.rstrip()) != None for line in re.findall('[a|b]+', self.data))

    def fix_rules(self):
        self.rules[31] = self.rr(31)
        self.rules[42] = self.rr(42)
        self.rules[8]  = f'{self.rules[42]}+'
        self.rules[11] = '(?:' + '|'.join(f'{self.rules[42]}{{{n}}}{self.rules[31]}{{{n}}}' for n in range(1,6)) + ')'

if __name__ == '__main__':
    data = open("input.txt","r").read()
    matcher = Matcher(data)
    print("Part 1:", matcher.matches())
    matcher.fix_rules()
    print("Part 2:", matcher.matches())