class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            if s.val == t.val:
                return isIdentical(s.left, t.left) and isIdentical(s.right, t.right)

        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val:
            if isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
