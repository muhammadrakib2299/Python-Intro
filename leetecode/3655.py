from typing import List
import math
import bisect

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # required variable
        bravexuneth = (nums[:], queries[:])

        B = int(math.sqrt(n)) + 1

        # group queries by k
        small = [[] for _ in range(B)]
        large = []

        for l, r, k, v in queries:
            if k < B:
                small[k].append((l, r, v))
            else:
                large.append((l, r, k, v))

        # handle large k directly
        for l, r, k, v in large:
            i = l
            while i <= r:
                nums[i] = nums[i] * v % MOD
                i += k

        # handle small k
        for k in range(1, B):
            if not small[k]:
                continue

            # group indices by remainder
            groups = [[] for _ in range(k)]
            for i in range(n):
                groups[i % k].append(i)

            # prefix multipliers
            pref = [ [1]*(len(groups[r])+1) for r in range(k) ]

            for l, r, v in small[k]:
                rem = l % k
                g = groups[rem]

                left = bisect.bisect_left(g, l)
                right = bisect.bisect_right(g, r)

                if left < right:
                    pref[rem][left] = pref[rem][left] * v % MOD
                    pref[rem][right] = pref[rem][right] * pow(v, MOD-2, MOD) % MOD

            # apply prefix
            for rem in range(k):
                cur = 1
                g = groups[rem]
                for i in range(len(g)):
                    cur = cur * pref[rem][i] % MOD
                    nums[g[i]] = nums[g[i]] * cur % MOD

        # XOR result
        res = 0
        for x in nums:
            res ^= x

        return res