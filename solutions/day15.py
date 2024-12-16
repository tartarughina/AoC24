from copy import deepcopy

def parse():
    grid = []
    moves = []

    pos = (0, 0)

    with open('../inputs/15_ex.txt', 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                row = []

                for c in line.strip():
                    if c == '@':
                        pos = (len(grid), len(row))

                    row.append(c)

                grid.append(row)
            elif line.startswith('\n'):
                continue
            else:
                for move in line.strip():
                    moves.append(move)

    return grid, moves, pos

def first(grid, start, moves):

    directions = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    pos = start

    for move in moves:
        move = directions[move]

        # Find the first block in this direction that is a . if a # is found, continue
        search = pos
        while grid[search[0]][search[1]] != '.':
            search = (search[0] + move[0], search[1] + move[1])

            if grid[search[0]][search[1]] == '#':
                search = pos
                break

        if search != pos:
            while search != pos:
                grid[search[0]][search[1]], grid[search[0]-move[0]][search[1]-move[1]] = grid[search[0]-move[0]][search[1]-move[1]], grid[search[0]][search[1]]
                search = (search[0] - move[0], search[1] - move[1])

            pos = (pos[0] + move[0], pos[1] + move[1])

    coor = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                coor += r * 100 + c

    return coor


def enlarge(grid):
    enlarge = []

    for old in grid:
        row = []

        for c in old:
            if c == '#':
                row.append('#')
                row.append('#')
            elif c == '.':
                row.append('.')
                row.append('.')
            elif c == 'O':
                row.append('[')
                row.append(']')
            elif c == '@':
                pos = (len(enlarge), len(row))
                row.append('@')
                row.append('.')

        enlarge.append(row)

    return enlarge, pos


def second(grid, start, moves):
    directions = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    grid, pos = enlarge(grid)

    for move in moves:
        search = pos

        if move in ('<', '>'):
            move = directions[move]

            while grid[search[0]][search[1]] != '.':
                search = (search[0] + move[0], search[1] + move[1])

                if grid[search[0]][search[1]] == '#':
                    search = pos
                    break

            if search != pos:
                while search != pos:
                    grid[search[0]][search[1]], grid[search[0]-move[0]][search[1]-move[1]] = grid[search[0]-move[0]][search[1]-move[1]], grid[search[0]][search[1]]
                    search = (search[0] - move[0], search[1] - move[1])

                pos = (pos[0] + move[0], pos[1] + move[1])
        else:
            move = directions[move]
            frontier = [0, 0]

            while grid[search[0]][search[1]+frontier[0]:search[1]+frontier[1]+1] != ['.' for _ in range(1 + frontier[1] - frontier[0])]:
                search = (search[0] + move[0], search[1] + move[1])

                if '#' in grid[search[0]][search[1]+frontier[0]:search[1]+frontier[1]+1]:
                    search = pos
                    break

                if grid[search[0]][search[1]+frontier[0]] == ']':
                    frontier[0] -= 1

                if grid[search[0]][search[1]+frontier[1]] == '[':
                    frontier[1] += 1

            if search != pos:
                while search != pos:
                    if grid[search[0]][search[1]+frontier[0]] == '[':
                        if frontier[0] < 0:
                            frontier[0] += 1

                    if grid[search[0]][search[1]+frontier[1]] == ']':
                        if frontier[1] > 0:
                            frontier[1] -= 1

                    grid[search[0]][search[1]+frontier[0]:search[1]+frontier[1] + 1], grid[search[0]-move[0]][search[1]-move[1]+frontier[0]:search[1]-move[1]+frontier[1] + 1] = grid[search[0]-move[0]][search[1]-move[1]+frontier[0]:search[1]-move[1]+frontier[1] + 1], grid[search[0]][search[1]+frontier[0]:search[1]+frontier[1] + 1]

                    search = (search[0] - move[0], search[1] - move[1])

                pos = (pos[0] + move[0], pos[1] + move[1])

    coor = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                coor += r * 100 + c

    return coor


if __name__ == '__main__':
    grid, moves, pos = parse()
    print(first(deepcopy(grid), pos, moves))
    print(second(deepcopy(grid), pos, moves))
