class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, el in enumerate(nums):
            if el not in seen.keys():
                seen[el] = i
            elif el in seen.keys():
                return True
        return False
