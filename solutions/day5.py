from collections import defaultdict, deque

def parse():
    neighbors = defaultdict(set)
    updates = []

    with open("day5.txt", "r") as f:
        lines = f.readlines()
        rules = True

        for line in lines:
            if line == "\n":
                rules = False
                continue

            if rules:
                line = line.strip()
                before, after = line.split('|')

                neighbors[before].add(after)
            else:
                updates.append(line.strip().split(','))

    return neighbors, updates

def apply_rules(rules, update):
    printed = set()

    for page in update:
        if rules[page].isdisjoint(printed):
            printed.add(page)
        else:
            return 0

    return int(update[len(update) // 2])


def first():
    rules, updates = parse()
    running = 0

    for update in updates:
        running += apply_rules(rules, update)

    return running


def filter_wrong(rules, update):
    printed = set()

    for page in update:
        if rules[page].isdisjoint(printed):
            printed.add(page)
        else:
            return True

    return False


def reorder(rules, update):
    # Assume that everything has been printed
    printed = set(update)
    new_order = []

    queue = deque(update)

    while queue:
        page = queue.popleft()

        if rules[page].isdisjoint(printed):
            printed.remove(page)
            new_order.append(page)
        else:
            queue.append(page)

    return int(new_order[len(new_order) // 2])

def second():
    rules, updates = parse()

    wrong = []

    running = 0

    for update in updates:
        if filter_wrong(rules, update):
            wrong.append(update)

    for update in wrong:
        running += reorder(rules, update)

    return running


if __name__ == "__main__":
    print(first())
    print(second())
