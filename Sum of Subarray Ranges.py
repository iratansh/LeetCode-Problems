class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min_stack = []
        min_sum = 0

        for i in range(len(nums) + 1):
            while min_stack and nums[min_stack[-1]] > (nums[i] if i < len(nums) else -float("Inf")):
                j = min_stack.pop()
                last = min_stack[-1] if min_stack else -1
                min_sum += (j - last) * (i - j) * nums[j]
            min_stack.append(i)
            
            
        max_stack = []
        max_sum = 0
        for i in range(len(nums) + 1):
            while max_stack and nums[max_stack[-1]] < (nums[i] if i < len(nums) else float("Inf")):
                j = max_stack.pop()
                last = max_stack[-1] if max_stack else -1
                max_sum += (j - last) * (i - j) * nums[j]
            max_stack.append(i)
        
        return max_sum - min_sum
