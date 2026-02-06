class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If numRows is 1 or less, no zigzag pattern is needed.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to hold the strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string and place characters into the correct row
        for char in s:
            rows[current_row] += char
            # If we're at the top or bottom row, change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down depending on the direction
            current_row += 1 if going_down else -1
        
        # Join all rows to form the final string
        return ''.join(rows)
