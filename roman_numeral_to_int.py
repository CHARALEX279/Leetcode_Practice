class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        conversion = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        array_version = []
        for x in s:
            array_version.append(conversion[x])


        i = 0
        j = 1
        total = 0
        while i != len(array_version):
            if j == len(array_version):
                total += array_version[i]
                
            elif array_version[j] > array_version[i]:
                total += array_version[j] - array_version[i]
                i += 1
                j +=1
            else: total += array_version[i]
            i +=1
            j +=1
        
        return total
