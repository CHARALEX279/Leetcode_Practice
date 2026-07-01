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
        
