class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            stack = []
            while True: 
                while root: 
                    if root.right is not None: 
                        stack.append(root.right) 
                    stack.append(root) 
                    root = root.left 
                root = stack.pop() 
                if (root.right is not None and stack and
                    stack[-1] == root.right): 
                    stack.pop()
                    stack.append(root) 
                    root = root.right 
                else: 
                    ans.append(root.val) 
                    root = None
                if (len(stack) <= 0): 
                        break
            return ans 
        return 
