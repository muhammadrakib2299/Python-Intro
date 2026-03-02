from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        
        # Initialize sets and collect empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
        
        def backtrack(index: int) -> bool:
            if index == len(empty):
                return True  # solved
            
            r, c = empty[index]
            box = (r // 3) * 3 + (c // 3)
            
            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
                    # place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)
                    
                    if backtrack(index + 1):
                        return True
                    
                    # undo (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)
            
            return False
        
        backtrack(0)