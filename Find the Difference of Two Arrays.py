class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1, ans2 = set(), set()
        res = []
        for num in nums1:
            if num in nums2 or num in ans1:
                continue
            else:
                ans1.add(num)
        
        for num in nums2:
            if num in nums1 or num in ans2:
                continue
            else:
                ans2.add(num)
        
        res.append(list(ans1))
        res.append(list(ans2))
        return res
        
