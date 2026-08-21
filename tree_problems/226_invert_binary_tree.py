#dfs solution, go all the way down, swap left and right, return root

#base case
def dfs(root):
  if not root:
    return
  
  root.right, root.left = self.dfs(root.left) and self.dfs(root.right)
  return root
