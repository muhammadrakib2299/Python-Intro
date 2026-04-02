from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[j][k]: current row
        dp = [[-float('inf')] * 3 for _ in range(n)]
        
        # Initialize (0,0)
        if coins[0][0] >= 0:
            dp[0][0] = coins[0][0]
        else:
            dp[0][0] = coins[0][0]      # no neutralization
            dp[0][1] = 0               # use neutralization
        
        # First row
        for j in range(1, n):
            for k in range(3):
                if dp[j-1][k] == -float('inf'):
                    continue
                
                # no neutralization
                dp[j][k] = max(dp[j][k], dp[j-1][k] + coins[0][j])
                
                # neutralize if possible
                if coins[0][j] < 0 and k < 2:
                    dp[j][k+1] = max(dp[j][k+1], dp[j-1][k])
        
        # Remaining rows
        for i in range(1, m):
            new_dp = [[-float('inf')] * 3 for _ in range(n)]
            
            # First column
            for k in range(3):
                if dp[0][k] == -float('inf'):
                    continue
                
                # no neutralization
                new_dp[0][k] = max(new_dp[0][k], dp[0][k] + coins[i][0])
                
                # neutralize
                if coins[i][0] < 0 and k < 2:
                    new_dp[0][k+1] = max(new_dp[0][k+1], dp[0][k])
            
            # Rest of row
            for j in range(1, n):
                for k in range(3):
                    # from top
                    if dp[j][k] != -float('inf'):
                        new_dp[j][k] = max(new_dp[j][k], dp[j][k] + coins[i][j])
                        if coins[i][j] < 0 and k < 2:
                            new_dp[j][k+1] = max(new_dp[j][k+1], dp[j][k])
                    
                    # from left
                    if new_dp[j-1][k] != -float('inf'):
                        new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k] + coins[i][j])
                        if coins[i][j] < 0 and k < 2:
                            new_dp[j][k+1] = max(new_dp[j][k+1], new_dp[j-1][k])
            
            dp = new_dp
        
        return max(dp[n-1])