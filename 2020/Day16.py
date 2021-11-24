#! python3
import re
import time

class Ticket():
    def __init__(self, fields, ticket_num):
        self.fields = [int(x) for x in fields]
        self.invalid = []
        self.ticket_num = ticket_num

    def get_invalid(self, valid):
        for f in self.fields:
            if f not in valid:
                self.invalid.append(f)


def get_fields(raw_rules):
    split_rules = raw_rules.split('\n')
    fields = set()
    sorted_fields = []
    for i, rule in enumerate(split_rules):
        sorted_fields.append(set())
        res = re.findall(r'\d+-\d+', split_rules[i])
        for j, r in enumerate(res):
            nums = r.split('-')
            field_range = set(range(int(nums[0]), int(nums[1])+1))
            fields.update(field_range)
            sorted_fields[i].update(field_range)
    return fields, sorted_fields


def error_rate(rules, tickets):
    valid_fields, field_rules = get_fields(rules)
    invalid = []
    valid_tickets = []
    for line in tickets:
        t = Ticket(line.strip().split(','), tickets.index(line))
        t.get_invalid(valid_fields)
        if t.invalid:
            invalid.extend(t.invalid)
        else:
            valid_tickets.append(t)
    return sum(invalid), valid_tickets, field_rules


if __name__ == '__main__':
    with open('input-Day16.txt') as f:
        text = f.read().strip().split('\n\n')

    ticket_rule_text = text[0].strip()
    my_ticket = text[1].strip().split(':\n')[1]
    nearby_tickets = text[2].strip().split('\n')[1:]

    error_rate, valid_tickets, rules = error_rate(ticket_rule_text, nearby_tickets)
    print(error_rate)

    confirmed_ticket_fields = []
    possible_ticket_fields = [set(range(len(rules))) for _ in rules]
    # use set intersections to compare possibilities
    t0 = time.perf_counter()
    for t in valid_tickets:
        field_possibilities = []
        for i, f in enumerate(t.fields):
            ticket_field_set = set()
            for j, r in enumerate(rules):
                if f in r:
                    ticket_field_set.add(j)
            field_possibilities.append(ticket_field_set)
            possible_ticket_fields[i].intersection(field_possibilities[i])


    t1 = time.perf_counter()
    print(t1 - t0)
