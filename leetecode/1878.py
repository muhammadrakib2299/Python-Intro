from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):
                res.add(grid[r][c])  # k = 0

                k = 1
                while r-k >= 0 and r+k < m and c-k >= 0 and c+k < n:
                    s = 0

                    # top -> right
                    i, j = r-k, c
                    for t in range(k):
                        s += grid[i+t][j+t]

                    # right -> bottom
                    i, j = r, c+k
                    for t in range(k):
                        s += grid[i+t][j-t]

                    # bottom -> left
                    i, j = r+k, c
                    for t in range(k):
                        s += grid[i-t][j-t]

                    # left -> top
                    i, j = r, c-k
                    for t in range(k):
                        s += grid[i-t][j+t]

                    res.add(s)
                    k += 1

        return sorted(res, reverse=True)[:3]