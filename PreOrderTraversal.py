class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            stack = []
            curr = root
            final_result = []
            while (len(stack) or curr != None):
                while (curr != None):
                    final_result.append(curr.val)
                    if (curr.right != None):
                        stack.append(curr.right)
                    curr = curr.left
                if (len(stack) > 0):
                    curr = stack[-1]
                    stack.pop()
            return final_result
        return None
