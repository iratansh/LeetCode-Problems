class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indexed = sorted([(start, i) for i, (start, end) in enumerate(intervals)]) # sort intervals based on their start time

        res = []
        for i in range(len(intervals)): 
            l, r = 0, len(intervals) - 1
            candidate_index = -1
            while l <= r:
                mid = (l + r) // 2
                if indexed[mid][0] >= intervals[i][1]:
                    candidate_index = indexed[mid][1]
                    r = mid - 1
                else:
                    l = mid + 1
            
            res.append(candidate_index)   
        return res
