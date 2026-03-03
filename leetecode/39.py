from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # i (not i+1) because we can reuse the same element
                backtrack(i, remaining - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return result