class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""
        
        count = 0
        start = 0
        parts = []
        
        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            # Found a balanced special substring
            if count == 0:
                # Recursively process inside
                inner = self.makeLargestSpecial(s[start + 1:i])
                parts.append('1' + inner + '0')
                start = i + 1
        
        # Sort in descending order for lexicographically largest result
        parts.sort(reverse=True)
        
        return ''.join(parts)