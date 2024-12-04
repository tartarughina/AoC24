def parse():
    ret = []

    with open('day4.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            ret.append(line.strip())

    return ret

def first():
    grid = parse()

    rows = len(grid)
    cols = len(grid[0])

    moves = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    targets = ['X', 'M', 'A', 'S']

    matches = [0]

    def dfs(r,c,move,target):
        if targets[target] == 'S' and grid[r][c] == 'S':
            matches[0] += 1
            return

        dc, dr = moves[move]
        if 0 <= dr + r < rows and 0 <= dc + c < cols and grid[dr+r][dc+c] == targets[target+1]:
            dfs(dr+r, dc+c, move, target+1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == targets[0]:
                for i in range(len(moves)):
                    dfs(r, c, i, 0)

    return matches[0]

def second():
    grid = parse()

    rows = len(grid)
    cols = len(grid[0])

    matches = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':
                if 0 < r < rows - 1 and 0 < c < cols - 1:
                    if (
                        (grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S') or (grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M')
                    ) and (
                        (grid[r+1][c-1] == 'M'  and grid[r-1][c+1] == 'S') or (grid[r+1][c-1] == 'S'  and grid[r-1][c+1] == 'M')
                    ):
                        matches += 1

    return matches


if __name__ == '__main__':
    print(first())
    print(second())
