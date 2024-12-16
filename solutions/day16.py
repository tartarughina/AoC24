from heapq import heappush, heappop

def parse():
    grid = []
    start = (0,0)

    with open('../inputs/16_ex.txt', 'r') as f:
        for line in f.readlines():
            row = []

            for c in line.strip():
                if c == 'S':
                    start = (len(grid), len(row))

                row.append(c)

            grid.append(row)

    return grid, start


def first(grid, start):
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    def djikstra():
        visited = set()
        queue = [(0, 0, start[0], start[1])]

        while queue:
            dist, facing, r, c = heappop(queue)

            if grid[r][c] == 'E':
                return dist

            visited.add((r,c))

            for dir, (dr, dc) in enumerate(directions):
                new_pos = (r + dr, c + dc)

                if new_pos in visited:
                    continue

                if grid[new_pos[0]][new_pos[1]] == '#':
                    continue

                cost = 1 if dir - facing == 0 else 1001
                heappush(queue, (dist + cost, dir, new_pos[0], new_pos[1]))

        return -1
    
    return djikstra()


def second(grid, start):
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    def djikstra():
        places = 0
        visited = {}
        queue = [(0, 0, start[0], start[1], 1)]

        while queue:
            dist, facing, r, c, tiles = heappop(queue)

            if grid[r][c] == 'E':
                return dist

            visited[(r,c, facing)] = dist

            for dir, (dr, dc) in enumerate(directions):
                new_pos = (r + dr, c + dc)

                if (new_pos[0], new_pos[1], dir) in visited:
                    if visited[(new_pos[0], new_pos[1], dir)] == dist:
                        places += tiles
                    continue

                if grid[new_pos[0]][new_pos[1]] == '#':
                    continue

                cost = 1 if dir - facing == 0 else 1001
                heappush(queue, (dist + cost, dir, new_pos[0], new_pos[1], tiles + 1))

        return places
    
    return djikstra()


if __name__ == '__main__':
    grid, start = parse()

    print(first(grid, start))
    print(second(grid, start))

