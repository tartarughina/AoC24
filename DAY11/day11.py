def parse():
    stones = []

    with open('day11.txt', 'r') as f:


        for line in f.readline().strip().split(' '):
            stones.append(int(line))

    return stones


def first(stones, k):

    for _ in range(k):
        step = []

        for stone in stones:
            if stone == 0:
                step.append(1)
            elif len(str(stone)) & 1 == 0:
                str_stone = str(stone)
                m = len(str_stone) // 2

                step.append(int(str_stone[:m]))
                step.append(int(str_stone[m:]))
            else:
                step.append(stone * 2024)

        stones = step

    return len(stones)

if __name__ == "__main__":
    stones = parse()

    print(first(stones[:], 25))
    print(first(stones[:], 75))
