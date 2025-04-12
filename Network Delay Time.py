class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in times:
            adj[u - 1].append((v - 1, w))  # make 0-indexed

        pq = [(0, k - 1)]  # (time, node), 0-indexed
        visit = set()
        time = 0

        while pq:
            dist, node = heapq.heappop(pq)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, dist)
            for nei, weight in adj[node]:
                if nei not in visit:
                    heapq.heappush(pq, (dist + weight, nei))

        return time if len(visit) == n else -1
