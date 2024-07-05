class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        ans = nums[0]

        while start <= end:
            if nums[start] < nums[end]:
                ans = min(ans, nums[start])
                break

            mid = (start + end) // 2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        
        return ans
