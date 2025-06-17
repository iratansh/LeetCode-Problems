class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmp = {0: -1}
        running_sum = 0

        for i, el in enumerate(nums):
            running_sum += el
            r = running_sum if k == 0 else running_sum % k
            if (r in hashmp and (i - hashmp[r]) >=2):
                return True
            if r not in hashmp:
                hashmp[r] = i
        return False
