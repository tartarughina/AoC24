from functools import cache
from collections import defaultdict

def parse():
    stones = []

    with open('../inputs/11.txt', 'r') as f:


        for line in f.readline().strip().split(' '):
            stones.append(int(line))

    return stones

@cache
def apply_rule(kind):
    if kind == 0:
        return (1, None)
    elif len(str(kind)) & 1 == 0:
        str_kind = str(kind)
        m = len(str_kind) // 2

        return (int(str_kind[:m]), int(str_kind[m:]))
    else:
        return (kind * 2024, None)


def first(stones, k):
    counter = defaultdict(int)

    for stone in stones:
        counter[stone] += 1

    for step in range(k):
        step_counter = defaultdict(int)

        for key, val in counter.items():
            kind, kind2 = apply_rule(key)

            step_counter[kind] += val

            if kind2 != None:
                step_counter[kind2] += val

        counter = step_counter

    return sum(counter.values())

if __name__ == "__main__":
    stones = parse()

    print(first(stones, 25))
    print(first(stones, 75))
