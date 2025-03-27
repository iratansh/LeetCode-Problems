class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize the sliding window with two pointers, one for left and one for right
        l, r = 0, len(arr) - 1
        
        # Move the right pointer to make the window size k
        while r - l + 1 > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1  # Remove right element if the left is closer to x
            else:
                l += 1  # Otherwise, remove the left element
        
        # Now we have the k closest elements, return them sorted
        return arr[l:r+1]
