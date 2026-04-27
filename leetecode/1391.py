from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # दिशा मैप: type -> allowed directions
        dirs = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }
        
        # reverse check (neighbor must connect back)
        def is_connected(x1, y1, x2, y2):
            for dx, dy in dirs[grid[x2][y2]]:
                if x2 + dx == x1 and y2 + dy == y1:
                    return True
            return False
        
        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if is_connected(x, y, nx, ny):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False