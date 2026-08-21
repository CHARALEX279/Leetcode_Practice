class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for j in range(len(nums2)+1)] for i in range(len(nums1)+1)]
        max_length = 0
        for i in range(len(nums1)-1, -1, -1):
            for j in range(len(nums2)-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    max_length = max(max_length, dp[i][j]) #return the length
                else:
                    dp[i][j] = 0 # simply set to zero, if we set it to whatever is bigger, we get the wrong number. idk why though
        return max_length

  # nums1 = [0,1,1,1,1]
  # nums2 = [1,0,1,0,1]
