class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #make an empty string
        #pop end of first string into beginning of empty string
        #check if strings are ==
        x = str(x)
        n = len(x) - 1
        new_s = ""
        for i in range(n, -1, -1):
            new_s = new_s + x[i]

        if new_s == x:
            return True

        return False 
