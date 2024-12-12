from collections import deque

def parse():
    grid = []

    with open('../inputs/12_ex.txt', 'r') as f:
        for line in f.readlines():
            row = []

            for val in line.strip():
                row.append(val)

            grid.append(row)

    return grid


def first(grid):
    rows = len(grid)
    cols = len(grid[0])

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(s_r, s_c, seed):
        area = 0
        perim = 0

        visited = set()
        queue = deque([(s_r,s_c)])
        grid[s_r][s_c] = '|'
        visited.add((s_r, s_c))

        while queue:
            r,c = queue.popleft()

            perimeter = 4
            for dr, dc in moves:
                if 0 <= dr+r < rows and 0 <= dc+c < cols:
                    if grid[dr+r][dc+c] == seed:
                        grid[dr+r][dc+c] = '|'
                        visited.add((dr+r, dc+c))
                        queue.append((dr+r, dc+c))
                        perimeter -= 1
                    elif (dr+r, dc+c) in visited:
                        perimeter -= 1

            perim += perimeter
            area += 1

        return area * perim

    price = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '|':
                price += bfs(r, c, grid[r][c])

    return price


if __name__ == '__main__':
    grid = parse()

    print(first(grid))
