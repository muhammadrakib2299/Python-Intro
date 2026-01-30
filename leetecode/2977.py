class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        INF = 10**18

        # 1) Collect all strings in rules
        strs = set(original) | set(changed)
        strs = list(strs)
        idx = {s: i for i, s in enumerate(strs)}
        m = len(strs)

        # 2) Floyd–Warshall
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            i, j = idx[o], idx[c]
            dist[i][j] = min(dist[i][j], w)

        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF:
                    continue
                for j in range(m):
                    if dist[k][j] == INF:
                        continue
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        # 3) Precompute valid substring lengths
        valid_lengths = set(len(s) for s in original)

        # 4) DP
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            # No-op if characters already match
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            # Try only valid substring lengths
            for L in valid_lengths:
                j = i + L
                if j > n:
                    continue

                s = source[i:j]
                t = target[i:j]

                if s in idx and t in idx:
                    d = dist[idx[s]][idx[t]]
                    if d != INF:
                        dp[j] = min(dp[j], dp[i] + d)

        return -1 if dp[n] == INF else dp[n]
