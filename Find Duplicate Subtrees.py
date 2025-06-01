# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        freq = defaultdict(int)
        dups = []

        def dfs(node):
            if not node:
                return "#"
            
            left_serial = dfs(node.left)
            right_serial = dfs(node.right)

            serial = f"{node.val},{left_serial},{right_serial}"
            freq[serial] += 1
            if freq[serial] == 2:
                dups.append(node)
            return serial


        dfs(root)
        return dups
