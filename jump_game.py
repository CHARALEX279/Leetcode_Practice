class Solution:
    def canJump(self, nums: List[int]) -> bool:
        possible_jumps = 0
        for n in nums:
            if possible_jumps < 0:
                return False
            elif n > possible_jumps:
                possible_jumps = n
            possible_jumps -= 1 #we've moved forward at least once, so subtract one

        return True
#or
        # max_jumps = 0
        # for i, n in enumerate(nums):
        #     if i > max_jumps:
        #         return False
        #     max_jumps = max(max_jumps, i+n)
        # return True
#shift the "goal post" to shift it
