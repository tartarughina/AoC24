def breaking_rule(inc, ln, rn) -> bool:
    return (ln > rn if inc else ln < rn) or abs(ln - rn) not in (1,2,3)

def check_decreasing(line) -> bool:
    l = 0
    r = l + 1

    inc = line[l] < line[r]

    while r < len(line):
        ln = line[l]
        rn = line[r]

        if breaking_rule(inc, ln, rn):
            return False

        l = r
        r += 1

    return True

def first():
    with open('../inputs/2.txt', 'r') as f:
        lines = f.readlines()

        safe = 0

        for line in lines:
            if check_decreasing([int(x) for x in line.strip().split(' ')]):
                safe += 1

        print(safe)


def check_bad_level(line) -> bool:
    token = True
    l = 0
    r = l + 1

    inc = line[l] < line[r]

    while r < len(line):
        ln = line[l]
        rn = line[r]

        if breaking_rule(inc, ln, rn):
            if token:
                token = not token

                # At this point skip the next element
                if r == len(line) - 1:
                    return True

                res = [False, False]

                # Check if l = 0 and r = 2 or l = 1 and r = 2
                if l == 0:
                    res[0] = breaking_rule(line[0] < line[2], line[0], line[2])
                    res[1] = breaking_rule(line[1] < line[2], line[1], line[2])

                    if res == [True, True]:
                        return False
                    elif res == [True, False]:
                        inc = line[1] < line[2]
                    elif res == [False, True]:
                        inc = line[0] < line[2]

                    l = 2
                    r = l + 1
                    continue

                # Maintain rn and take l - 1
                # Maintain ln and take r + 1
                res[0] = breaking_rule(inc, line[l-1], rn)
                res[1] = breaking_rule(inc, ln, line[r+1])

                if res == [True, True]:
                    return False
                elif res == [True, False]:
                    if l == 1:
                        inc = line[1] < line[2]

                    l = r
                    r += 1
                    continue

                l = r + 1
                r += 2

                continue
            else:
                return False

        l = r
        r += 1

    return True

def second():
    with open('../inputs/2.txt', 'r') as f:
        lines = f.readlines()

        safe = 0

        for line in lines:
            if check_bad_level([int(x) for x in line.strip().split(' ')]):
                safe += 1

        print(safe)


if __name__ == '__main__':
    # first()
    second()
