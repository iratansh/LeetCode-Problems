class Solution:
    def minPartitions(self, n: str) -> int:
        largest = float("-inf")
        for num in n:
            if int(num) > largest:
                largest = int(num)
        return largest
