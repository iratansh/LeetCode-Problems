# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + ',' + right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree_list = data.split(',')

        def trav():
            nodeNext = tree_list.pop(0)
            if nodeNext == 'None':
                return None
            nodeNew = TreeNode(int(nodeNext))
            nodeNew.left = trav()
            nodeNew.right = trav()
            return nodeNew
        return trav()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
