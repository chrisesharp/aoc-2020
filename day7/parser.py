import re

class Parser:
    def __init__(self, data):
        self.bags = {}
        self.parse(data)
    
    def parse(self, data):
        for rule in data:
            tokens = self.tokenize(rule)
            holder = tokens.pop(0)
            dependents = self.bags.get(holder,set())
            for token in tokens:
                if token := token.strip():
                    dependents.add(token)
            self.bags[holder] = dependents

    def tokenize(self, rule):
        return re.split((" bags contain | bag[s., ]*"), rule)
    
    def containers(self, target_bag):
        return set([bag for bag in self.bags for container in self.bags[bag] if target_bag in container])
    
    def all_containers(self, target_bag):
        results = set()
        bags = self.containers(target_bag)
        while bags:
            bag = bags.pop()
            results.add(bag)
            bags |= set([new_bag for new_bag in self.containers(bag) if new_bag not in results])
        return results
    
    def contains(self, container):
        count = 0
        contents = list(self.bags.get(container, set()))
        while contents:
            bag = contents.pop()
            num, bag = re.split((" "), bag, 1)
            if num != "no" and (num := int(num)):
                count += num
                contents += [new_bag for new_bag in self.bags.get(bag, set())]*num
        return count
    
if __name__ == '__main__':
    rules = open("input.txt","r").readlines()
    my_parser = Parser(rules)
    all_containers = my_parser.all_containers("shiny gold")
    print("Part 1:",len(all_containers))
    print("Part 2:", my_parser.contains("shiny gold"))
