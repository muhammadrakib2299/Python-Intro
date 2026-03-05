class Solution:
    def minOperations(self, s: str) -> int:
        mismatch1 = 0  # pattern starting with '0' -> 0101...
        mismatch2 = 0  # pattern starting with '1' -> 1010...
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    mismatch1 += 1
                if s[i] != '1':
                    mismatch2 += 1
            else:
                if s[i] != '1':
                    mismatch1 += 1
                if s[i] != '0':
                    mismatch2 += 1
        
        return min(mismatch1, mismatch2)