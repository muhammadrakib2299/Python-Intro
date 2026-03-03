from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # sort to handle duplicates
        result = []
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # pruning
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                # i + 1 because each number can only be used once
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return result