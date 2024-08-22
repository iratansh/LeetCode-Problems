class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order_list = []
        def inorderTraversal(node):
            if node:
                # Traverse left subtree
                inorderTraversal(node.left)
                
                # Visit node
                order_list.append(node.val)
                
                # Traverse right subtree
                inorderTraversal(node.right)
                
        inorderTraversal(root)
        return order_list[k - 1] if order_list else 0
