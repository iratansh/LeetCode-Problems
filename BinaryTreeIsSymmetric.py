class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            def checker(root1, root2):
                if root1 is None and root2 is None:
                    return True
                elif not root1 and root2 or root1 and not root2 or root1.val != root2.val:
                    return False
                left = checker(root1.left, root2.right)
                right = checker(root1.right, root2.left)
                return left and right
            return checker(root.left, root.right)
        return True
