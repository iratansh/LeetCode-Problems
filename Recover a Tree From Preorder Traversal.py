# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # depth is represented by the number of dashes from root! not from previous node
        # the idea looks to be to continuously populate the left subtree as the number of dashes increases from the previous number (by 1) 
        # then if the number of dashes decreases (ie the last number had 3 dashes and then the current number has 2 dashes) we backtrack to the previous node ON THAT DEPTH (which may require multiple recursive calls) and populate the right subtree 
        stack = [] # (node, depth)
        i, n = 0, len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            node = TreeNode(val)

            while stack and stack[-1][-1] >= depth: # pop until we reach the parent level
                stack.pop()
            if stack:
                parent, _ = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

            stack.append((node, depth))
        return stack[0][0]
            

        


                


