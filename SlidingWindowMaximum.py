class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        ans = []
        l_pointer, r_pointer = 0, 0

        while r_pointer < len(nums):
            while queue and nums[queue[-1]] < nums[r_pointer]:
                queue.pop()
            queue.append(r_pointer)

            if l_pointer > queue[0]:
                queue.popleft()

            if r_pointer + 1 >= k:
                ans.append(nums[queue[0]])
                l_pointer += 1
  
            r_pointer += 1
        return ans
