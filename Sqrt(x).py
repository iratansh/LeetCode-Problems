class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        lowerIndex = 0
        upperIndex = x
        ans = 1

        while lowerIndex <= upperIndex:
            middleIndex = (lowerIndex + upperIndex) // 2
            if x >= middleIndex*middleIndex:
                ans = middleIndex
                lowerIndex = middleIndex + 1
            else:
                upperIndex = middleIndex - 1
        return ans
