class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a seenMap: int_val: num_times_seen
        seenMap = {}
        for num in nums:
            if num in seenMap:
                seenMap[num] +=1
            else:
                seenMap[num] = 1


        #create an array of lists at length plus 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in seenMap.items():
            buckets[val].append(key)
        
        #list of top two to return
        k_items = []

        #iterate backwards over the array of list

        #   if item at array !=list, append item that we found into retun list 
        # if return list == k, return
