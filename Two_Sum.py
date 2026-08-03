class Solution(object):https://github.com/CHARALEX279/Leetcode_Practice/security
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seenMap = {} #diffValue: index
        for index, value in enumerate(nums):
            diff = target - value
            if diff in seenMap:
                return([seenMap[diff], index])
            seenMap[value]=index
        return()  

#second attempt! reviewed because i couldn't get the white board to work. remember, the value is the key! and the index is the value
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen_map:
                return [seen_map[diff], i]
            else:
                seen_map[nums[i]] = i
