from collections import defaultdict
from heapq import heappop, heappush


def parse():
    grid = []
    start = None
    end = None

    with open('../inputs/20.txt', 'r') as f:
        for line in f.readlines():
            row = []

            for c in line.strip():
                if c == '#':
                    row.append(-1)
                    continue

                if c == 'S':
                    start = (len(grid), len(row))
                elif c == 'E':
                    end = (len(grid), len(row))

                row.append(float('inf'))

            grid.append(row)

    return grid, start, end


def first(grid, start, end):
    queue = [(0, start, [start])]

    rows = len(grid)
    cols = len(grid[0])

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    good_path = []

    while queue:
        dist, (r, c), path = heappop(queue)

        if (r,c) == end:
            grid[r][c] = dist
            good_path = path
            break

        grid[r][c] = dist

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and dist < grid[nr][nc]:
                heappush(queue, (dist + 1, (nr, nc), path + [(nr, nc)]))

    # The grid, as it is, contains only the best path ideally speaking
    #
    # Traverse the ideal path from the end and look only for situations where the next block is a wall
    # curr + 1 == -1 and the next block in that direction is a number lower than the current one, the picoseconds save
    # are curr - cheat - 2

    shortcuts = defaultdict(int)

    for r, c in good_path:
        for dr, dc in moves:
            wr, wc = r + dr, c + dc

            if 0 <= wr < rows and 0 <= wc < cols and grid[wr][wc] == -1:
                sr, sc = wr + dr, wc + dc

                if 0 <= sr < rows and 0 <= sc < cols and grid[sr][sc] != -1 and grid[sr][sc] < grid[r][c]:
                    if grid[r][c] - grid[sr][sc] - 2 >= 100:
                        shortcuts[grid[r][c] - grid[sr][sc] - 2] += 1

    return sum(shortcuts.values()), good_path


def second(grid, path):
    # Manhattan distance among the other positions of the path? Whaaaaaaaaat?
    #
    shortcuts = 0

    for i in range(len(path)):
        r, c = path[i]

        for j in range(i+1, len(path)):
            cr, cc = path[j]

            dist = abs(r - cr) + abs(c - cc)

            if dist <= 20:
                if grid[cr][cc] - grid[r][c] - dist >= 100:
                    shortcuts += 1

    return shortcuts


if __name__ == '__main__':
    grid, start, end = parse()

    shortcuts, path = first(grid, start, end)
    print(shortcuts)

    print(second(grid, path))
