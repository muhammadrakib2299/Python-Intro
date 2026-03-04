from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Multiply from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                
                # positions in result
                p1 = i + j
                p2 = i + j + 1
                
                # Add to existing value
                total = mul + result[p2]
                
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Convert to string and remove leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        
        return result_str