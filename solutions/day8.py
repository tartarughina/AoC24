from collections import defaultdict

def parse():
    antennas = defaultdict(list)
    occupied = set()
    rows = 0
    cols = 0
    with open('../inputs/8.txt', 'r') as f:
        lines = f.readlines()

        rows = len(lines)
        cols = len(lines[0].strip())

        for r, line in enumerate(lines):
            for c, val in enumerate(line.strip()):
                if val == '.':
                    continue
                else:
                    antennas[val].append((r,c))
                    occupied.add((r,c))

    return antennas, occupied, rows, cols


def first(antennas, occupied, rows, cols):
    antinodes = set()

    for loc in antennas.values():
        for i in range(len(loc)):
            for j in range(i+1, len(loc)):
                dr = abs(loc[i][0] - loc[j][0])
                dc = abs(loc[i][1] - loc[j][1])

                new_pos = [[0,0], [0,0]]

                if loc[i][0] > loc[j][0]:
                    new_pos[0][0] = loc[i][0] + dr
                    new_pos[1][0] = loc[j][0] - dr
                else:
                    new_pos[0][0] = loc[i][0] - dr
                    new_pos[1][0] = loc[j][0] + dr

                if loc[i][1] > loc[j][1]:
                    new_pos[0][1] = loc[i][1] + dc
                    new_pos[1][1] = loc[j][1] - dc
                else:
                    new_pos[0][1] = loc[i][1] - dc
                    new_pos[1][1] = loc[j][1] + dc

                for pos in new_pos:
                    if pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >= cols:
                        continue

                    antinodes.add(tuple(pos))

    return len(antinodes)


def second(antennas, rows, cols):
    antinodes = set()

    for loc in antennas.values():
        for i in range(len(loc)):
            for j in range(i+1, len(loc)):
                dr = abs(loc[i][0] - loc[j][0])
                dc = abs(loc[i][1] - loc[j][1])

                i_d = [dr,dc]
                j_d = [dr,dc]


                if loc[i][0] > loc[j][0]:
                    j_d[0] *= -1
                else:
                    i_d[0] *= -1

                if loc[i][1] > loc[j][1]:
                    j_d[1] *= -1
                else:
                    i_d[1] *= -1

                i_pos = [loc[i][0], loc[i][1]]
                while 0 <= i_pos[0] < rows and 0 <= i_pos[1] < cols:
                    antinodes.add(tuple(i_pos))

                    i_pos[0] += i_d[0]
                    i_pos[1] += i_d[1]

                j_pos = [loc[j][0], loc[j][1]]
                while 0 <= j_pos[0] < rows and 0 <= j_pos[1] < cols:
                    antinodes.add(tuple(j_pos))

                    j_pos[0] += j_d[0]
                    j_pos[1] += j_d[1]

    return len(antinodes)


if __name__ == "__main__":
    antennas, occupied, rows, cols = parse()

    print(first(antennas, occupied, rows, cols))
    print(second(antennas, rows, cols))
