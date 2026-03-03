class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case
        if n == 1:
            return "0"
        
        length = (1 << n) - 1          # 2^n - 1
        mid = (length // 2) + 1        # middle position
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # mirrored position in previous string
            mirrored = mid - (k - mid)
            bit = self.findKthBit(n - 1, mirrored)
            # invert the bit
            return "1" if bit == "0" else "0"