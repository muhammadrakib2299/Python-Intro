class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left (skip the first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                # Odd → +1 and /2
                steps += 2
                carry = 1
            else:
                # Even → just /2
                steps += 1
        
        # If carry remains, one final step
        return steps + carry