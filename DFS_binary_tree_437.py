# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # helper function - make each node feel like a root :)
    def countPath(self, node: Optional[TreeNode], targetSum:int) -> int:
        #base case
        if node is None:
            return 0
        #action
        if node.val == targetSum:
            path = 1
        else:
            path = 0
        #recall
        left_paths = self.countPath(node.left, targetSum - node.val)
        right_paths = self.countPath(node.right, targetSum - node.val)

        return path + left_paths + right_paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
