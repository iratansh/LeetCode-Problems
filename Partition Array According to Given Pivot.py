class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # move all elements less than pivot before pivot and the elements greater than pivot
        # move the elements equal to pivot between the elements less than and greater than pivot - group privot elemtns together
        # maintain the ordering of the orginal nums still though
        l, e, g = [], [], []

        for num in nums:
            if num < pivot:
                l.append(num)
            elif num == pivot:
                e.append(num)
            else:
                g.append(num)
        return l + e + g
            
