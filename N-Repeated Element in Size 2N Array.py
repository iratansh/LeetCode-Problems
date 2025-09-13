class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        freq = Counter(nums)
        for key, val in freq.items():
            if val == n:
                return key
