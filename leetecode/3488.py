from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        res = []
        
        for q in queries:
            v = nums[q]
            arr = pos[v]
            
            if len(arr) == 1:
                res.append(-1)
                continue
            
            i = bisect.bisect_left(arr, q)
            
            ans = float('inf')
            
            # Check next element (skip self)
            if i + 1 < len(arr):
                j = arr[i + 1]
                d = abs(j - q)
                ans = min(ans, min(d, n - d))
            
            # Check previous element
            if i - 1 >= 0:
                j = arr[i - 1]
                d = abs(j - q)
                ans = min(ans, min(d, n - d))
            
            # Circular neighbors
            # first and last wrap
            j = arr[0]
            if j != q:
                d = abs(j - q)
                ans = min(ans, min(d, n - d))
            
            j = arr[-1]
            if j != q:
                d = abs(j - q)
                ans = min(ans, min(d, n - d))
            
            res.append(ans)
        
        return res