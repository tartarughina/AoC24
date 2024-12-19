from heapq import heappop, heappush


def parse():
    rows, cols = 71, 71
    grid = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    with open('../inputs/18.txt', 'r') as f:
        for _ in range(1024):
            line = f.readline().strip()
            coor = line.split(',')

            grid[int(coor[0])][int(coor[1])] = -1

    return rows, cols, grid


def first(rows, cols, grid):

    queue = [(0, 0, 0)]

    while queue:
        dist, x, y = heappop(queue)

        if grid[x][y] <= dist:
            continue

        grid[x][y] = dist

        if x == rows-1 and y == cols-1:
            return dist

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
                heappush(queue, (dist + 1, nx, ny))

    return grid[rows-1][cols-1]


def second(rows, cols):
    start = 1024
    end = 0
    grid = {}
    lines = []

    with open('../inputs/18.txt', 'r') as f:
        lines = f.readlines()

        end = len(lines)

        for i in range(end):
            line = lines[i].strip()
            coor = line.split(',')

            grid[(int(coor[0]), int(coor[1]))] = i

    def bfs(grid, m):
        queue = [(0, 0, 0)]
        visited = set()

        while queue:
            dist, x, y = heappop(queue)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            if x == rows - 1 and y == cols - 1:
                return dist

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if (nx, ny) in grid and grid[(nx, ny)] <= m:
                        continue

                    heappush(queue, (dist + 1, nx, ny))

        return -1

    while start < end:
        m = start + (end - start) // 2

        res = bfs(grid, m)

        if res > -1:
            start = m + 1
        else:
            end = m

    return lines[start]

if __name__ == '__main__':
    rows, cols, grid = parse()

    print(first(rows, cols, grid))
    print(second(rows, cols).strip())
