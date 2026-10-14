from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1

        visit = set()
        q = deque()
        q.append((0, 0))
        visit.add((0, 0))
        length = 1

        neighbors = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr == rows or nc == cols
                            or (nr, nc) in visit or grid[nr][nc] == 1):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1