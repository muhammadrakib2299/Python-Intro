def maxDotProduct(nums1, nums2):
    n, m = len(nums1), len(nums2)

    # Initialize DP table with very small values
    dp = [[float('-inf')] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            product = nums1[i] * nums2[j]

            # Option 1: take only this pair
            dp[i][j] = product

            # Option 2: extend previous subsequence
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i][j], product + dp[i-1][j-1])

            # Option 3: skip nums1[i]
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j])

            # Option 4: skip nums2[j]
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])

    return dp[n-1][m-1]

nums1 = [2,1,-2,5]
nums2 = [3,0,-6]

maxDotProduct(nums1, nums2)