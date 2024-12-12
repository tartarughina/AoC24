from collections import deque

def parse():
    grid = []

    with open('../inputs/12.txt', 'r') as f:
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


def second(grid):
    rows = len(grid)
    cols = len(grid[0])

    # 0 -> Right
    # 1 -> Down
    # 2 -> Left
    # 3 -> Up

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(s_r, s_c, seed):
        area = 0
        corner = 0

        visited = set()
        queue = deque([(s_r,s_c)])

        grid[s_r][s_c] = '|'
        visited.add((s_r, s_c))

        while queue:
            r,c = queue.popleft()

            mask = 1
            corner_type = 0
            for dr, dc in moves:
                if 0 <= dr+r < rows and 0 <= dc+c < cols:
                    if grid[dr+r][dc+c] == seed:
                        grid[dr+r][dc+c] = '|'
                        visited.add((dr+r, dc+c))

                        queue.append((dr+r, dc+c))
                    elif (dr+r, dc+c) in visited:
                        pass
                    else:
                        corner_type |= mask
                else:
                    corner_type |= mask

                mask <<= 1
            # corner_type
            if corner_type in (3, 6, 9, 12):
                corner += 1

                # Check other corner for inner
                if corner_type == 3 and grid[r-1][c-1] != seed and (r-1, c-1) not in visited:
                    corner += 1
                elif corner_type == 6 and grid[r-1][c+1] != seed and (r-1, c+1) not in visited:
                    corner += 1
                elif corner_type == 9 and grid[r+1][c-1] != seed and (r+1, c-1) not in visited:
                    corner += 1
                elif corner_type == 12 and grid[r+1][c+1] != seed and (r+1, c+1) not in visited:
                    corner += 1
            elif corner_type in (7, 11, 13, 14):
                corner += 2
            elif corner_type == 15:
                corner += 4
            elif corner_type in (1, 2, 4, 8):
                if corner_type == 1:
                    if grid[r-1][c-1] != seed and (r-1, c-1) not in visited:
                        corner += 1

                    if grid[r+1][c-1] != seed and (r+1, c-1) not in visited:
                        corner += 1
                elif corner_type == 2:
                    if grid[r-1][c-1] != seed and (r-1, c-1) not in visited:
                        corner += 1

                    if grid[r-1][c+1] != seed and (r-1, c+1) not in visited:
                        corner += 1
                elif corner_type == 4:
                    if grid[r-1][c+1] != seed and (r-1, c+1) not in visited:
                        corner += 1

                    if grid[r+1][c+1] != seed and (r+1, c+1) not in visited:
                        corner += 1
                elif corner_type == 8:
                    if grid[r+1][c-1] != seed and (r+1, c-1) not in visited:
                        corner += 1

                    if grid[r+1][c+1] != seed and (r+1, c+1) not in visited:
                        corner += 1

            area += 1

        return area * corner

    price = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '|':
                price += bfs(r, c, grid[r][c])

    return price


if __name__ == '__main__':
    print(first(parse()))
    print(second(parse()))
