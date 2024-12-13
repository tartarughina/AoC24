A_cost = 3
B_cost = 1

def parse():
    machines = []

    with open('../inputs/13.txt', 'r') as f:
        config = {}

        for line in f.readlines():
            if line.startswith('B'):
                rest, y = line.split(', ')
                rest = rest.split(' ')
                x = rest[-1]
                button = rest[1].replace(':', '')

                config[button] = (int(x[2:]), int(y[2:]))
            elif line.startswith('P'):
                rest, y = line.split(', ')
                x = rest = rest.split(' ')[-1]
                config['P'] = (int(x[2:]), int(y[2:]))
            else:
                machines.append(config)
                config = {}

        machines.append(config)

    return machines


def first(machines, second=False):
    tokens = 0

    for config in machines:
        ax, ay = config['A']
        bx, by = config['B']
        prize_x, prize_y = config['P']

        if second:
            prize_x += 10000000000000
            prize_y += 10000000000000

        a = round((prize_y - ((by * prize_x) / bx)) / (ay - ((by * ax) / bx)))
        b = round((prize_x - ax * a) / bx)

        if ax * a + bx * b == prize_x and ay * a + by * b == prize_y:

            tokens += a * A_cost + b * B_cost

    return tokens


if __name__ == '__main__':
    machines = parse()
    print(first(machines))
    print(first(machines, second=True))
