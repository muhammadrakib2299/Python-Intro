from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0
        
        # add sentinel to flush stack at end
        heights.append(0)
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                
                # width calculation
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                
                max_area = max(max_area, h * w)
            
            stack.append(i)
        
        return max_area