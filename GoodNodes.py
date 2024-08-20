class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, val):
            if node:
                res = 1 if node.val >= val else 0
                val = max(val, node.val)
                res += dfs(node.left, val)
                res += dfs(node.right, val)
                return res
            return 0
        return dfs(root, root.val)
