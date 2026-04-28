# Definition for a binary tree node.
#final attempt: 0,1,2 coverage approach with post order DFS
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cameras = 0
    #0 == needs camera
    #1 == give camera
    #2 == covered

    def DFS(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 2
        left = self.DFS(node.left)
        right = self.DFS(node.right)
        if left == 0 or right == 0: #needs a camera
            self.cameras += 1
            return 1
        if left == 1 or right == 1:
            return 2
        return 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #base
        if self.DFS(root) == 0:
            self.cameras +=1      
        return self.cameras


#first attempt! i approached it as there's only 1 camera per family, but that was hard to track in DFS. Maybe if i tried BFS and kept track of the levels?
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #helper
    def isFamily(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        if node and (node.left or node.right): 
            if node.left and node.right is None:
                if node.left.left or node.left.right:
                    camera = 1
                else:
                    camera = 0
            if node.right and node.left is None:
                if node.right.left or node.right.right:
                    camera = 1
                else:
                    camera = 0
        else:
            camera = 0
        left_cameras = self.isFamily(node.left)
        right_cameras = self.isFamily(node.right)

        return camera + left_cameras + right_cameras

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #base
        if root is None:
            return 0
        
        #action
        root_camera = self.isFamily(root)
        left_cameras = self.minCameraCover(root.left)
        right_cameras = self.minCameraCover(root.right)

        return root_camera + left_cameras + right_cameras


        
