def get_rules(data):
    rules = {}
    for line in data.splitlines():
        field, vals = line.split(':')
        outputs = []
        for seat_range in [seats for seats in vals.split(' or ')]:
            from_seat, to_seat = seat_range.split('-') 
            outputs.append(list(range(int(from_seat),int(to_seat)+1)))
        rules[field] = outputs
    return rules

def parse_ticket(line):
    return list(map(int, [seat for seat in line.split(',')]))

def parse_tickets(data):
    return list(map(parse_ticket, data[1:]))

def get_ticket(ticket_fields, fields_map):
    ticket = {}
    for i, val in enumerate(ticket_fields):
        ticket[fields_map[i]]= val
    return ticket

def compute_result(ticket, fields):
    count = 1
    for field in ticket:
        if field.find("departure") == 0:
            count *= ticket[field]
    return count

class Scanner:
    def __init__(self, data):
        data = data.split("\n\n")
        self.rules = get_rules(data[0])
        self.your_ticket = parse_tickets(data[1].splitlines())[0]
        self.nearby_tickets = parse_tickets(data[2].splitlines())
        self.valid_tickets = []

    def get_error_rate(self):
        result = []
        for ticket in self.nearby_tickets:
            ticket_valid = True
            for field in ticket:
                field_valid = len([field for ranges in self.rules.values() for seat_range in ranges if field in seat_range])
                if not field_valid:
                    result.append(field)
                    ticket_valid = False
                    break
            if ticket_valid:
                self.valid_tickets.append(ticket)
        return sum(result)
    
    def get_field_sets(self):
        field_lists = [False] * len(self.your_ticket)
        for ticket in self.valid_tickets:
            for i, field_val in enumerate(ticket):
                valid_fieldnames = set()
                for fieldname in self.rules:
                    if len([field_val for seat_range in self.rules[fieldname] if field_val in seat_range]):
                        valid_fieldnames.add(fieldname)
                field_lists[i] = valid_fieldnames if not field_lists[i] else field_lists[i] & valid_fieldnames
        return field_lists

    def match_fields(self):
        field_sets = self.get_field_sets()
        fields_map = [False] * len(self.your_ticket)
        matched = set()
        while len(matched) < len(self.your_ticket):
            for i, fields in enumerate(field_sets):
                if len(fields) == 1:
                    field = fields_map[i] = fields.pop()
                    matched.add(field)
                elif len(fields) > 1:
                    field_sets[i] -= matched
        self.fields_map = fields_map
        return fields_map
    
    def get_ticket(self):
        return get_ticket(self.your_ticket, self.fields_map)


if __name__ == '__main__':
    data = open("input.txt","r").read()
    scanner = Scanner(data)
    print("Part 1:",scanner.get_error_rate())
    fields = scanner.match_fields()
    ticket = scanner.get_ticket()
    print("Part 2:", compute_result(ticket, fields))
