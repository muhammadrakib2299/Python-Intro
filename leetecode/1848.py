from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')  # Initialize with a very large number
        
        for i, num in enumerate(nums):
            if num == target:
                distance = abs(i - start)
                if distance < min_distance:
                    min_distance = distance
        
        return min_distance