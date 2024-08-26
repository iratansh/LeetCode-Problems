class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-el for el in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))

            if x != y:
                heapq.heappush(stones, (y - x))
        
        stones.append(0)
        return abs(stones[0])
