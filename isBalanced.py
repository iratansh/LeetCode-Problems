class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(node):
            if not node:
                return 0
            left, right = height(node.left), height(node.right)
            return 1 + max(left, right)
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) 
