from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots, distance, walls):
        robots = sorted(zip(robots, distance))
        walls.sort()
        
        n = len(robots)
        
        # Precompute intervals
        left_intervals = []
        right_intervals = []
        
        for i, (r, d) in enumerate(robots):
            # Left
            L = r - d
            if i > 0:
                L = max(L, robots[i-1][0] + 1)
            R = r
            
            lidx = bisect_left(walls, L)
            ridx = bisect_right(walls, R)
            left_intervals.append((L, R, lidx, ridx))
            
            # Right
            L = r
            R = r + d
            if i < n - 1:
                R = min(R, robots[i+1][0] - 1)
            
            lidx = bisect_left(walls, L)
            ridx = bisect_right(walls, R)
            right_intervals.append((L, R, lidx, ridx))
        
        # Greedy: try both directions per robot
        covered = set()
        res = 0
        
        for i in range(n):
            # Count new walls for left
            lL, lR, l1, l2 = left_intervals[i]
            left_gain = sum(1 for j in range(l1, l2) if j not in covered)
            
            # Count new walls for right
            rL, rR, r1, r2 = right_intervals[i]
            right_gain = sum(1 for j in range(r1, r2) if j not in covered)
            
            # Choose better direction
            if left_gain >= right_gain:
                for j in range(l1, l2):
                    if j not in covered:
                        covered.add(j)
                        res += 1
            else:
                for j in range(r1, r2):
                    if j not in covered:
                        covered.add(j)
                        res += 1
        
        return res