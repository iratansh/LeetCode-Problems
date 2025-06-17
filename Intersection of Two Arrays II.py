class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) <= len(nums2):
            hashmp = Counter(nums1)
            for num in nums2:
                if hashmp[num] > 0:
                    res.append(num)
                    hashmp[num] -= 1

        else:
            hashmp = Counter(nums2)
            for num in nums1:
                if hashmp[num] > 0:
                    res.append(num)
                    hashmp[num] -= 1
        return res
