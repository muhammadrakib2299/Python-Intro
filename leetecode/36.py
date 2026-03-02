from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
<<<<<<< HEAD
                if val == '.':
=======
                if val == ".":
>>>>>>> 1b62e0a307f4da2f7b5cdf842cd4d6e56a1af6bd
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)
                
<<<<<<< HEAD
                if (val in rows[r] or 
                    val in cols[c] or 
=======
                # Check duplicate
                if (val in rows[r] or
                    val in cols[c] or
>>>>>>> 1b62e0a307f4da2f7b5cdf842cd4d6e56a1af6bd
                    val in boxes[box_index]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        
        return True