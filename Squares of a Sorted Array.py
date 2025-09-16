class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two-pointer approach l, r where left is at the start and right is at the end
        # for all ints such that abs(i^2) such that i < 0 compare it with the elements at j such that j are the elements at the end of nums and then place the elements in the correct position. The window for j to n would be the number of negative elements
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        
        pos = len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] ** 2
                l += 1
            else:
                res[pos] = nums[r] ** 2
                r -= 1
            pos -= 1
        return res
