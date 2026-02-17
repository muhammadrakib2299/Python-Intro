class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # Mapping of closing to opening brackets
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:  # Closing bracket
                # Pop top element if stack not empty, else assign dummy value
                top = stack.pop() if stack else '#'
                
                if mapping[char] != top:
                    return False
            else:  # Opening bracket
                stack.append(char)
        
        return not stack
