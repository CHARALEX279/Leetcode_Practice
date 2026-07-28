#dfs solution, go all the way down, swap left and right, return root

#base case
def dfs(root):
  if not root:
    return
  
  if root.left and root.right:
    newLeft = root.right.val
    newRight = root.left.val
    root.left = newLeft
    root.right = newRight
    
    dfs(root.left)
    dfs(root.right)
return self.dfs(root.left) and self.dfs(root.right)
