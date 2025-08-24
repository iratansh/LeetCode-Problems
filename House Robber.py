class Solution:
    def rob(self, nums: List[int]) -> int:
        table = [] # should store max values going from 0 and incrementing by 2 and max values from 1 incrementing by 2
        table.append(nums[0])
        table.append(nums[1])

        for i in range(2, len(nums)):
            # calculate new value from first route first
            total = table[i - 2] + nums[i]
            table.append(total) 

            # calculate new value from second route
            total = table[i - 1] + nums[i]
            table.append(total)

        return max(table[-1], table[-2])
