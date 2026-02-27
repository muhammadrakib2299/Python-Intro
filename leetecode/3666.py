class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        
        if zeros == 0:
            return 0
        
        if k > n:
            return -1
        
        # If k is even
        if k % 2 == 0:
            # x*k is always even
            if zeros % 2 == 1:
                return -1
            return (zeros + k - 1) // k
        
        # If k is odd
        x = (zeros + k - 1) // k
        if x % 2 != zeros % 2:
            x += 1
        return x