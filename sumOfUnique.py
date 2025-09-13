class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # sum the elements with freqency = 1
        
        freq = Counter(nums)
        keys = [key for key, val in freq.items() if val == 1]
        return sum(keys)
