class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0

        for el in nums:
            if el - 1 not in nums:
                consecutive = 0
                while el + consecutive in nums:
                    consecutive += 1
                count = max(consecutive, count)
        return count
        
