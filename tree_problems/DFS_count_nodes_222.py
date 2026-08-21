# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root:
            node_root = 1 # it could also return 1 in the return, but i like that i know i'm counting the root
        
        return node_root + self.countNodes(root.left) + self.countNodes(root.right)
        
