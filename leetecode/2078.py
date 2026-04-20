from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Case 1: compare with first element
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                dist1 = j
                break
        
        # Case 2: compare with last element
        for i in range(n):
            if colors[i] != colors[n - 1]:
                dist2 = (n - 1) - i
                break
        
        return max(dist1, dist2)