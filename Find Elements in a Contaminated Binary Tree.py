# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.bt = root
        self.bt.val = 0
        self.values = set()
        def recover(node):
            if not node:
                return
            self.values.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
                recover(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                recover(node.right)
        recover(self.bt)

    def find(self, target: int) -> bool:
        if target in self.values:
            return True
        return False
