def parse():
    grid = []

    with open('../inputs/10.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            curr = []

            for c in line.strip():
                curr.append(int(c))

            grid.append(curr)

    return grid

def first(grid):
    rows = len(grid)
    cols = len(grid[0])

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    tot = 0

    visited = set()

    def dfs(r, c, next, start):
        if grid[r][c] == 9 and (start, (r,c)) not in visited:
            visited.add((start, (r,c)))
            return 1

        ret = 0
        for dr, dc in moves:
            if 0 <= dr + r < rows and 0 <= dc + c < cols and grid[dr + r][dc + c] == next:
                ret += dfs(dr + r, dc + c, next + 1, start)

        return ret

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                tot += dfs(r, c, 1, (r,c))

    return tot


def second(grid):
    rows = len(grid)
    cols = len(grid[0])

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    tot = 0

    def dfs(r, c, next):
        if grid[r][c] == 9:
            return 1

        ret = 0
        for dr, dc in moves:
            if 0 <= dr + r < rows and 0 <= dc + c < cols and grid[dr + r][dc + c] == next:
                ret += dfs(dr + r, dc + c, next + 1)

        return ret

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                tot += dfs(r, c, 1)

    return tot


if __name__ == "__main__":
    grid = parse()

    print(first(grid))
    print(second(grid))
