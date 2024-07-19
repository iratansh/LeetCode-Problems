class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for el in nums:
            if el not in nums_set:
                nums_set.add(el)
            elif el in nums_set:
                return el
