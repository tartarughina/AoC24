from collections import defaultdict

def first_part():
    l1 = []
    l2 = []

    with open('day1_1.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            first, second = line.strip().split('   ')

            l1.append(int(first))
            l2.append(int(second))

    l1.sort()
    l2.sort()

    running = 0
    for first, second in zip(l1, l2):
        running += abs(first - second)

    print(running)

def second_part():
    l1 = set()
    l2 = defaultdict(int)

    with open('day1_1.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            first, second = line.strip().split('   ')

            l1.add(first)
            l2[second] += 1

    running = 0
    for first in l1:
        running += l2[first] * int(first)

    print(running)

if __name__ == '__main__':
    # first_part()
    second_part()
