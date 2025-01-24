class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_num = len(nums)
        hash_map = Counter(nums)
        res = []
        
        for i in range(1, max_num + 1):
            if i not in hash_map:
                res.append(i)
        return res
