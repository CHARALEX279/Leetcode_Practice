#smart skipping! move the pointers down

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        output = []
        i = s.find(a)
        j = s.find(b)

        while i != -1 and j != -1:
            if abs(j - i) <=k:
                output.append(i)
                i = s.find(a, i+1)
            elif i > j: 
                j = s.find(b, i-k) #this moves j to 1 index after the last i was found
            else:
                i = s.find(a, j-k)
        return output
