wordBreak():
  dp = [False] * (len(s) + 1) # initializing the array
  dp[len(s) = True
  for in in range(len(s)-1, -1, -1)
    for w in wordDict:
      if i + len(w) <= len(s) and s[i : i+len(w)] == w:
        dp[i] = dp[i+len(w)] # this would be the possition in the array that is true
      if dp[i] == True:
        break
    return dp[0]
