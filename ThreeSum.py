class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, el in enumerate(nums):
            if i > 0 and el == nums[i - 1]:
                continue
            l_pointer, r_pointer = i + 1, len(nums) - 1

            while l_pointer < r_pointer:
                sum = el + nums[l_pointer] + nums[r_pointer]
                if sum > 0:
                    r_pointer -= 1
                elif sum < 0:
                    l_pointer += 1
                else:
                    ans.append([el, nums[l_pointer], nums[r_pointer]])
                    l_pointer += 1
                    while nums[l_pointer] == nums[l_pointer - 1] and l_pointer < r_pointer:
                        l_pointer += 1
 
        return ans
