from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def is_within_two_edits(w1, w2):
            diff = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        res = []
        
        for q in queries:
            for d in dictionary:
                if is_within_two_edits(q, d):
                    res.append(q)
                    break
        
        return res