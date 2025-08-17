# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # create the root as mentioned - max of the nums array
        # recurviely build the left subtree and right subtree - largest num in each resepective subarray becomes the root of the subtree
        # then the largest element to the left of the root becomes the roots left child and the largest element to the right of the root becomes the roots right child
        # need to think of a way to extract the largest element in each recursive call while still preserving the order of nums
        def recBuild(arr): # arr should be a subarray of nums
            if not arr:
                return None
            maxVal = max(arr)
            idx = arr.index(maxVal)
            root = TreeNode(maxVal)
            root.left = recBuild(arr[:idx])
            root.right = recBuild(arr[idx + 1:])
            return root
        return recBuild(nums)
