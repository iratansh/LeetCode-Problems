class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if not node:
                return -1
            left, right = dfs(node.left), dfs(node.right)
            nonlocal ans
            ans = max(ans, 2 + left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return ans
