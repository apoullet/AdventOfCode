import sys
import re

from dataclasses import dataclass


workflows, ratings = open(sys.argv[1]).read().strip().split('\n\n')

@dataclass
class Rating:
    x: int
    m: int
    a: int
    s: int
    
    def sum(self):
        return self.x + self.m + self.a + self.s

workflows = workflows.split('\n')
ratings   = ratings.split('\n')

def parse_workflows(workflows):
    parsed = {}

    for workflow in workflows:
        match = re.fullmatch(r'(.*)\{(.*)\}', workflow)
        if match is None:
            continue
        name, rules = match.group(1), match.group(2)
        parsed[name] = rules.split(',')

    return parsed

def parse_ratings(ratings):
    parsed = []

    for rating in ratings:
        x_str, m_str, a_str, s_str = re.findall(r'\d+', rating)
        parsed.append(Rating(int(x_str), int(m_str), int(a_str), int(s_str)))

    return parsed

workflows = parse_workflows(workflows)
ratings   = parse_ratings(ratings)

accepted_ratings = []

for rating in ratings:
    current = 'in'

    while current != 'A' and current != 'R':
        rule = workflows[current]

        for statement in rule:
            if ':' not in statement:
                current = statement
                break
            else:
                predicate, outcome = statement.split(':')

                letter, operator, value = predicate[0], predicate[1], int(predicate[2:])
                
                matches = False
                match letter:
                    case 'x':
                        matches = rating.x > value if operator == '>' else rating.x < value
                    case 'm':
                        matches = rating.m > value if operator == '>' else rating.m < value
                    case 'a':
                        matches = rating.a > value if operator == '>' else rating.a < value
                    case 's':
                        matches = rating.s > value if operator == '>' else rating.s < value
                if matches:
                    current = outcome
                    break

    if current == 'A':
        accepted_ratings.append(rating)

print(sum(map(lambda r:r.sum(), accepted_ratings)))

def add_ratings(x, m, a, s):
    return (
        (x[1]-x[0]+1 if x is not None else 4000) *
        (m[1]-m[0]+1 if m is not None else 4000) *
        (a[1]-a[0]+1 if a is not None else 4000) *
        (s[1]-s[0]+1 if s is not None else 4000)
    )

def get_total_combinations(rule, workflows, x=None, m=None, a=None, s=None):
    results = []
    for statement in rule:
        if statement == 'A':
            results.append(add_ratings(x, m, a, s))
            continue
        if statement == 'R':
            continue
        if ':' not in statement:
            results.append(get_total_combinations(workflows[statement], workflows, x, m, a, s))
            continue

        predicate, outcome = statement.split(':')
        letter, operator, value = predicate[0], predicate[1], int(predicate[2:])

        if operator == '>':
            match letter:
                case 'x':
                    if not x:
                        if outcome == 'A':
                            results.append(add_ratings((value+1, 4000), m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, (value+1, 4000), m, a, s))
                        x = (1, value)
                    elif x[0] > value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif x[1] > value:
                        if outcome == 'A':
                            results.append(add_ratings((value+1, x[1]), m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, (value+1, x[1]), m, a, s))
                        x = (x[0], value)
                case 'm':
                    if not m:
                        if outcome == 'A':
                            results.append(add_ratings(x, (value+1, 4000), a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, (value+1, 4000), a, s))
                        m = (1, value)
                    elif m[0] > value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif m[1] > value:
                        if outcome == 'A':
                            results.append(add_ratings(x, (value+1, m[1]), a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, (value+1, m[1]), a, s))
                        m = (m[0], value)
                case 'a':
                    if not a:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, (value+1, 4000), s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, (value+1, 4000), s))
                        a = (1, value)
                    elif a[0] > value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif a[1] > value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, (value+1, a[1]), s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, (value+1, a[1]), s))
                        a = (a[0], value)
                case 's':
                    if not s:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, (value+1, 4000)))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, (value+1, 4000)))
                        s = (1, value)
                    elif s[0] > value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif s[1] > value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, (value+1, s[1])))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, (value+1, s[1])))
                        s = (s[0], value)
        else:
            match letter:
                case 'x':
                    if not x:
                        if outcome == 'A':
                            results.append(add_ratings((1, value-1), m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, (1, value-1), m, a, s))
                        x = (value, 4000)
                    elif x[1] < value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif x[0] < value:
                        if outcome == 'A':
                            results.append(add_ratings((x[0], value-1), m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, (x[0], value-1), m, a, s))
                        x = (value, x[1])
                case 'm':
                    if not m:
                        if outcome == 'A':
                            results.append(add_ratings(x, (1, value-1), a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, (1, value-1), a, s))
                        m = (value, 4000)
                    elif m[1] < value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif m[0] < value:
                        if outcome == 'A':
                            results.append(add_ratings(x, (m[0], value-1), a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, (m[0], value-1), a, s))
                        m = (value, m[1])
                case 'a':
                    if not a:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, (1, value-1), s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, (1, value-1), s))
                        a = (value, 4000)
                    elif a[1] < value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif a[0] < value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, (a[0], value-1), s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, (a[0], value-1), s))
                        a = (value, a[1])
                case 's':
                    if not s:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, (1, value-1)))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, (1, value-1)))
                        s = (value, 4000)
                    elif s[1] < value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, s))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, s))
                    elif s[0] < value:
                        if outcome == 'A':
                            results.append(add_ratings(x, m, a, (s[0], value-1)))
                        elif outcome != 'R':
                            results.append(get_total_combinations(workflows[outcome], workflows, x, m, a, (s[0], value-1)))
                        s = (value, s[1])
    return sum(results)

combinations_count = get_total_combinations(workflows['in'], workflows)
print(combinations_count)
