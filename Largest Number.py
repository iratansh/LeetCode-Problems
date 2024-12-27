class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1  
            return 1

        for i, el in enumerate(nums):
            nums[i] = str(el)
        
        nums = sorted(nums, key=cmp_to_key(compare))
        
        return str(int("".join(nums)))
