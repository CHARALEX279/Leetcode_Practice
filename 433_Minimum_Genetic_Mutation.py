#initial approach. but this failed for test case 3. I need to use BFS
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        #loop over each letter in the start gene and end gene at once, if there is a difference, check the bank to see if those differences exsist, increase valid count

        #check if endgene is valid first, then if not return -1, else check difference between start and end
        valid = -1
        if endGene not in bank:
            #endGene is not a valid mutation
            return valid
        
        valid +=1
        startGeneList = list(startGene)
        endGeneList = list(endGene)
        for i in range(len(startGeneList)):
            if startGeneList[i] != endGeneList[i]:
                print("mutation found")
                print(startGeneList[i], endGeneList[i])
                valid += 1
                print(f"valid count: {valid}")

        return valid


        
