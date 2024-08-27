class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        new_nums = [-num for num in nums]
        heapq.heapify(new_nums)
        k -= 1

        while k > 0:
            heapq.heappop(new_nums)
            k -= 1
        return new_nums[0] * -1
