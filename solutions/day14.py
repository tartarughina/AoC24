from collections import defaultdict


def parse():
    robots = []

    with open('../inputs/14.txt') as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()

            pos, vel = line.split(' ')

            pos = pos[2:].split(',')
            vel = vel[2:].split(',')

            pos = [int(x) for x in pos]
            vel = [int(x) for x in vel]

            robots.append(pos + vel)

    return robots


def first(robots_in):
    rows = 103
    cols = 101

    grid = defaultdict(int)
    n = len(robots_in)

    robots = {}

    id = 0
    for px, py, vx, vy in robots_in:
        grid[(px, py)] += 1

        robots[id] = {
            'pos': (px, py),
            'vel': (vx, vy)
        }

        id += 1

    for _ in range(100):
        for id in range(n):
            px, py = robots[id]['pos']
            vx, vy = robots[id]['vel']

            grid[(px, py)] -= 1

            px = (px + vx) % cols

            if px < 0:
                px = cols + px

            py = (py + vy) % rows

            if py < 0:
                py = rows + py

            robots[id]['pos'] = (px, py)
            grid[(px, py)] += 1

    safety_factors = [0, 0, 0, 0]

    for (px, py), val in grid.items():
        if px < cols // 2 and py < rows // 2:
            safety_factors[0] += val
        elif px < cols // 2 and py > rows // 2:
            safety_factors[1] += val
        elif px > cols // 2 and py < rows // 2:
            safety_factors[2] += val
        elif px > cols // 2 and py > rows // 2:
            safety_factors[3] += val

    ret = 1

    for x in safety_factors:
        ret *= x

    return ret


def second(robots_in):
    rows = 103
    cols = 101

    grid = defaultdict(int)
    n = len(robots_in)

    robots = {}

    id = 0
    for px, py, vx, vy in robots_in:
        grid[(px, py)] += 1

        robots[id] = {
            'pos': (px, py),
            'vel': (vx, vy)
        }

        id += 1

    for i in range(10000):
        vis = [[0 for _ in range(cols)] for _ in range(rows)]

        for id in range(n):
            px, py = robots[id]['pos']
            vx, vy = robots[id]['vel']

            grid[(px, py)] -= 1

            px = (px + vx) % cols

            if px < 0:
                px = cols + px

            py = (py + vy) % rows

            if py < 0:
                py = rows + py

            robots[id]['pos'] = (px, py)
            grid[(px, py)] += 1

            vis[py][px] += 1

        with open(f'{i}.log', 'w') as f:
            for row in vis:
                f.write(''.join(['#' if x > 0 else '.' for x in row]) + '\n')


if __name__ == '__main__':
    robots = parse()

    print(first(robots))
    second(robots)
