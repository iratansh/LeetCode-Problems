class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        ans = end

        while start <= end:
            mid = (start + end) // 2
            hours = 0

            for el in piles:
                hours += math.ceil(el / mid)

            if hours <= h:
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1

        return ans
