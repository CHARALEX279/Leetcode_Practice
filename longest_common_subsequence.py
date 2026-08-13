class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recursive attempt. It works, but takes wayyyyy to long.
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
