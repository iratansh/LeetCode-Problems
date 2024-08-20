class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(el):
            s, e = 0, len(nums)
            while s < e:
                mid = (s + e) // 2
                if nums[mid] < el:
                    s = mid + 1
                else:
                    e = mid
            return s
        
        s = bs(target)
        e = bs(target + 1) - 1
    
        if s <= e:
            return [s, e]
        return [-1, -1]
