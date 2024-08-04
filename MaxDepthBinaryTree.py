class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_depth, r_depth = self.maxDepth(root.left), self.maxDepth(root.right)
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1
