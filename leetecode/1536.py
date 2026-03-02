from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Count trailing zeros
        trailing = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: Greedy placement
        for i in range(n):
            needed = n - 1 - i
            j = i
            
            # Find a row that satisfies requirement
            while j < n and trailing[j] < needed:
                j += 1
            
            if j == n:
                return -1
            
            # Bubble row upward
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps