class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        i = 0

        while i < len(nums):
            res.append((nums[i], nums[i + 1]))
            i += 2
        

        return sum(min(group) for group in res)
