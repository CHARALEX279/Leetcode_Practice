class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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



        # #DP approach
        # iniate a grid of text1 and text2 length
        # working backard, visit the grid at location i and j


        #if i and j are the same value, set that location to 1 + the value of the i+1 square and j+1 square
        #else, set the currnt dp[i][j] square to the square that is larger, [i+ 1][j] or [i][j+1]
