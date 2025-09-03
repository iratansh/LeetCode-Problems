class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # rearrange the elements in nums such that after each num, the next element has an opposite sign to the previous element
        # semi-two-pointer approach, split nums into 2 arrays - 1 for pos ints and 1 for neg ints. 
        # order doesn't matter in this question 
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res
