from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)
        window = {}
        
        have, need_count = 0, len(need)
        res = [-1, -1]
        res_len = float("inf")
        
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            
            if c in need and window[c] == need[c]:
                have += 1
            
            # Try shrinking
            while have == need_count:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # Remove from left
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""