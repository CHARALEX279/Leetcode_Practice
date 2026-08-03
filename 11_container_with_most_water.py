class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) - 1
        left = 0
        right = n
        max_area = 0

        while left < right:
            index_diff = right - left
            print("right:{0}".format(right))
            print("left:{0}".format(left))
            calc_area = index_diff * min(height[left], height[right])
            print(calc_area)
            if calc_area > max_area:
                max_area = calc_area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1    
        return max_area


#second attempt before reviewing the code! this worked, but time exceeded when running a large list:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area_height = min(height[i], height[j])
                area_width = abs(i-j)
                area_total = area_height * area_width
                max_water = max(max_water,area_total)
        return max_water
        
        
