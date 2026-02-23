class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        
        # Overflow case
        if dividend == MIN and divisor == -1:
            return MAX
        
        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Double the divisor until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        return -quotient if negative else quotient