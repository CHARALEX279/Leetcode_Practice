#only works half the time :P
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #base
        if root is None:
            return True
        #action
        if root.left is None and root.right is None and root:
            return True
        if root.left and root.right:
            if root.left.val < root.val < root.right.val:
                return True
            elif (root.left.val >= root.val) or (root.val >= root.right.val):
                return False
        if root.left and root and root.right is None:
            if root.left.val < root.val:
                return True
            elif (root.left.val >= root.val):
                return False
        if root.left is None and root and root.right:
            if root.val < root.right.val:
                return True
            elif (root.val >= root.right.val):
                return False
        #recall
        return self.isValidBST(root.left) or self.isValidBST(root.right)
