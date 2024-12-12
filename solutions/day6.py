def parse():
    obstacles = set()

    guard_pos = None
    # Copy the char representing the guard
    guard_face = None

    rows = None
    cols = None

    with open('../inputs/6.txt', 'r') as f:
        lines = f.readlines()

        rows = len(lines)
        cols = len(lines[0].strip())

        for row, line in enumerate(lines):
            for col, c in enumerate(line.strip()):
                if c == '.':
                    continue
                elif c == '#':
                    obstacles.add((row, col))
                else:
                    guard_pos = (row, col)
                    guard_face = c

    return obstacles, guard_pos, guard_face, rows, cols


def get_face(facing):
    if facing == '^':
        return 3
    elif facing == '>':
        return 0
    elif facing == 'v':
        return 1
    else:
        return 2


def first(obstacles, guard_pos, facing, rows, cols):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    tiles = set()

    tiles.add(guard_pos)

    while True:
        next_pos = (guard_pos[0] + moves[facing][0], guard_pos[1] + moves[facing][1])

        if next_pos in obstacles:
            facing = (facing + 1) % 4
        elif next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= cols:
            break
        else:
            guard_pos = next_pos
            tiles.add(guard_pos)

    return tiles


def test_loop(obstacles, guard_pos, facing, rows, cols):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    tiles = {}
    tiles[guard_pos] = facing
    steps = 0

    while True and steps < rows * cols * 4:
        next_pos = (guard_pos[0] + moves[facing][0], guard_pos[1] + moves[facing][1])

        if next_pos in obstacles:
            tiles[guard_pos] = facing
            facing = (facing + 1) % 4
        elif next_pos[0] < 0 or next_pos[0] >= rows or next_pos[1] < 0 or next_pos[1] >= cols:
            return False
        else:
            guard_pos = next_pos

            if guard_pos in tiles:
                if tiles[guard_pos] == facing:
                    return True
            else:
                tiles[guard_pos] = facing

        steps += 1

    return True


def second(obstacles, guard_pos, facing, rows, cols, visited):
    added = 0

    # Starting position cannot be used as an obstacle
    visited.remove(guard_pos)

    for i, pos in enumerate(visited):
        obstacles.add(pos)
        if test_loop(obstacles, guard_pos, facing, rows, cols):
            added += 1

        obstacles.remove(pos)

    return added

if __name__ == '__main__':
    obstacles, guard_pos, guard_face, rows, cols = parse()
    tiles = first(obstacles, guard_pos, get_face(guard_face), rows, cols)
    print(len(tiles))
    print(second(obstacles, guard_pos, get_face(guard_face), rows, cols, tiles))
