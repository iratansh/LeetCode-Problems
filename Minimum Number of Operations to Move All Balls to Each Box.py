class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = [int(b) for b in boxes] # convert the str in boxes to ints
        n = len(arr)
        res = [0] * n

        # Left -> right
        moves, count = 0, 0
        for i in range(n):
            res[i] += moves
            if arr[i] == 1:
                count += 1
            moves += count

        # Right -> left
        moves, count = 0, 0
        for i in range(n-1, -1, -1):
            res[i] += moves
            if arr[i] == 1:
                count += 1
            moves += count
        return res
