from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(start, parts, path):
            # If 4 parts formed
            if parts == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # Prune
            remaining_chars = len(s) - start
            remaining_parts = 4 - parts
            if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
                return
            
            # Try 1 to 3 digits
            for l in range(1, 4):
                if start + l > len(s):
                    break
                
                segment = s[start:start + l]
                
                # Leading zero check
                if len(segment) > 1 and segment[0] == '0':
                    continue
                
                # Value check
                if int(segment) > 255:
                    continue
                
                backtrack(start + l, parts + 1, path + [segment])
        
        backtrack(0, 0, [])
        return res