import unittest
from parser import Parser

class GameTest(unittest.TestCase):
    def test_parse_rules(self):
        data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
        rules = data.splitlines()
        my_parser = Parser(rules)
        tokens = my_parser.tokenize(rules[0])

        self.assertEqual("light red", tokens[0])
        self.assertEqual("1 bright white", tokens[1])
        self.assertEqual("2 muted yellow", tokens[2])
        all_containers = my_parser.all_containers("shiny gold")
        self.assertTrue("bright white" in all_containers)
        self.assertTrue("muted yellow" in all_containers)
        self.assertTrue("dark orange" in all_containers)
        self.assertTrue("light red" in all_containers)

    def test_parse_rules_all(self):
        data = """vibrant purple bags contain 3 faded maroon bags, 1 clear bronze bag, 5 striped black bags, 5 muted indigo bags.
"""
        rules = data.splitlines()
        my_parser = Parser(rules)
        all_containers = my_parser.all_containers("muted indigo")
        self.assertTrue("vibrant purple" in all_containers)
    
    def test_parse_rules_count(self):
        data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
        rules = data.splitlines()
        my_parser = Parser(rules)
        all_containers = my_parser.contains("shiny gold")
        self.assertEqual(32, all_containers)
    
    def test_parse_rules_count_2(self):
        data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
        rules = data.splitlines()
        my_parser = Parser(rules)
        all_containers = my_parser.contains("shiny gold")
        self.assertEqual(126, all_containers)
        
if __name__ == '__main__':
    unittest.main()
