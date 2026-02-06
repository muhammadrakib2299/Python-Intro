class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Check if x is negative
        sign = -1 if x < 0 else 1
        
        # Work with the absolute value of x
        x = abs(x)
        
        # Reverse the digits of x using string manipulation
        reversed_x = int(str(x)[::-1])
        
        # Apply the sign back if the number was negative
        reversed_x *= sign
        
        # Check if the reversed number is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
