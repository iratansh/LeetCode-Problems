class Solution:
    def scoreOfString(self, s: str) -> int:
        # convert s to an ascii representation 
        arr = [ord(char) for char in s]
        res = 0
        for i in range(1, len(arr)):
            res += abs(arr[i] - arr[i - 1])
        
        return res
