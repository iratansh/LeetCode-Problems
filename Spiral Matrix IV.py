# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]

        # di, dj (Directional Vectors) i - right/left, j - up/down
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start with "right"
        i, j = 0, 0  # Start position
        while head:
            res[i][j] = head.val  
            head = head.next
            ni, nj = i + dirs[dir_idx][0], j + dirs[dir_idx][1]
            if (ni < 0 or ni >= m or nj < 0 or nj >= n or res[ni][nj] != -1):
                dir_idx = (dir_idx + 1) % 4
                ni, nj = i + dirs[dir_idx][0], j + dirs[dir_idx][1]
            i, j = ni, nj
        return res
