class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # If total possible substrings is larger than string length, impossible
        if len(s) < k:
            return False
        
        needed = 1 << k  # 2^k
        seen = set()
        
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            if substring not in seen:
                seen.add(substring)
                needed -= 1
                if needed == 0:
                    return True
        
        return False