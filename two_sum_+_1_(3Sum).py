class Solution(object):
   def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    
    """
    triplets = []
    hashmap = {}

    if len(nums) < 3:
        return triplets

    else:
        sorted_nums = nums
        sorted_nums.sort()

        #make a list key of i & i plus 1, then make the sume of i & i plus one the value
        list_length = len(sorted_nums) - 1
        for i in range(list_length):
            key = []
            initial_sum = sorted_nums[i] + sorted_nums[i+1]
            key.append(sorted_nums[i])
            key.append(sorted_nums[i+1])

            #total = sorted_nums[i] + sorted_nums[i+1] - initial_sum

            tup_key = tuple(key)
            hashmap[tup_key] = initial_sum * -1


    

        for k in hashmap:
            val = hashmap[k]
            if val in sorted_nums:
                group = list(k)
                group.append(val)
                group.sort()
                if group not in triplets:
                    triplets.append(group)

        return triplets
        
