class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numSet = set(nums)
        return len(numSet) - (0 in numSet)
