class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive_len, negative_len, max_len = 0, 0, 0

        for num in nums:
            if num > 0:
                positive_len += 1
                negative_len = negative_len + 1 if negative_len > 0 else 0
            elif num < 0:
                new_positive_len = negative_len + 1 if negative_len > 0 else 0
                negative_len = positive_len + 1
                positive_len = new_positive_len
            else:
                positive_len, negative_len = 0, 0

            max_len = max(max_len, positive_len)
        
        return max_len
