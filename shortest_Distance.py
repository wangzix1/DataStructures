###https://blog.csdn.net/qq_37821701/article/details/108906696
### 0: empty land 1: building cannot pass through 2: obstacle
import math
import collections
###BFS try each empty land
class Solution:
    def shortestDistance(self, grid:List[List[int]])->int:
        m, n = len(grid), len(grid[0])
        num_buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_buildings += 1
        min_step = math.inf


        def helper(i, j):
            visited = set()
            buildings = set()
            q = collections.deque([(i,j, 0)])
            visited.add((i, j))
            total_step = 0
            dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

            while q:
                i, j, step = q.popleft()
                if grid[i][j]==1 and (i,j) not in buildings:
                    total_step+=step
                    buildings.add((i,j))
                if len(buildings) == num_buildings:
                    break
                if grid[i][j] != 1:
                    for d in dirs:
                        x = i+d[0]
                        y = j+d[1]
                        if 0 <= x < m and 0 <= y < n and (x,y) not in visited and grid[x][y] != 2:
                            q.apend((x,y))
                            visited.add((x, y))
            return total_step if len(buildings) == num_buildings else -1
                            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total_step = helper(i,j)
                    if total_step != -1 and min_step > total_step:
                        min_step = total_step
        return min_step if min_step != math.inf else -1
