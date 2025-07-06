class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(nums[i], i) for i in range(len(nums))]
        heapify(heap)
        for _ in range(k):
            val, i = heappop(heap)
            nums[i] = val * multiplier
            heappush(heap, (nums[i], i))
        return nums
