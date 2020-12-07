import re

class Parser:
    def __init__(self, data):
        self.bags = {}
        for rule in data:
            tokens = self.tokenize(rule)
            holder = tokens.pop(0)
            dependents = self.bags.get(holder,set())
            for token in tokens:
                token = token.strip()
                if token != '':
                    dependents.add(token)
            self.bags[holder] = dependents
        

    def tokenize(self, rule):
        return re.split((" bags contain | bag[s]*[.,]*[ ]*"), rule)
    
    def containers(self, target_bag):
        results = set()
        for bag, holds in self.bags.items():
            for container in holds:
                if target_bag in container:
                    results.add(bag)
        return results
    
    def all_containers(self, target_bag):
        results = set()
        bags = self.containers(target_bag)
        while bags:
            bag = bags.pop()
            results.add(bag)
            for new_bag in self.containers(bag):
                if new_bag not in results:
                    bags.add(new_bag)
        return results
    
    def contains(self, holding_bag):
        contents = list(self.bags.get(holding_bag,set()))
        count = 0
        while contents:
            bag = contents.pop()
            num, bag = re.split((" "), bag, 1)
            if num != "no" and int(num) > 0:
                num = int(num)
                count += num
                for i in range(num):
                    for new_bag in self.bags.get(bag, set()):
                        contents.append(new_bag)
        return count
    
if __name__ == '__main__':
    rules = open("input.txt","r").readlines()
    my_parser = Parser(rules)
    all_containers = my_parser.all_containers("shiny gold")
    print("Part 1:",len(all_containers))
    print("Part 2:", my_parser.contains("shiny gold"))
