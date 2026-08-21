#class Solution:
    #def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # #recursive attempt. It works, but takes wayyyyy to long.
        # i = 0
        # j = 0
        # count = 0
        # def LCS(i, j):
        #     if i > len(text1)-1 or j > len(text2)-1:
        #         return 0
        #     elif text1[i] == text2[j]:
        #         return 1 + LCS(i+1, j+1)
        #     else:
        #         return max(LCS(i+1, j), LCS(i, j+i))
        # count += LCS(i,j)
        # return count



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp =[[0 for j in range(len(text2) + 1)]for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                elif text1[i] != text2[j]:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
