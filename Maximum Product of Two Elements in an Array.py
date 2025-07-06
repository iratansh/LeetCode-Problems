class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # basically just use max heap property to find the 2 largest nums
        nums = [-num for num in nums]
        heapify(nums)
        num1 = heappop(nums) * -1
        num2 = heappop(nums) * -1
        res = (num1 - 1) * (num2 - 1)
        return res
