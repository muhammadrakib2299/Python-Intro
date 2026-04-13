class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[0] = 1  # Empty string
        dp[1] = 0 if s[0] == '0' else 1  # First character
        
        for i in range(2, n + 1):
            # Check single digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # Check two digits
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]