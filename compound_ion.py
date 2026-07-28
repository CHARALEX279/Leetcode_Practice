#Find the Compound Ion

#You are given a list of integers, where each number represents the electric charge of either a single ion or a compound ion.
#In this chemistry:
#* The charge of a compound ion is the sum of the charges of the ions it’s made from.
#* Exactly one number in the list is the charge of a compound ion formed by combining all other ions except one (the remaining ion is unused).
#Your task: Find and return the charge of the compound ion.


#example Input: [5, 1, 2, 3, 6]
#output : 6

#can you write out all possible combination of n elements:
#[ (5,1), (5,2), (5,3), (5,6), (1,2), (1,3), (1,6), (2,3), (2,6), (3,6)...] 
#[ (2,3,6)

given = [5, 1, 2, 3, 6]

for i in range(len(given)):
    for j in range(i+1, len(given)):
        print(given[i], given[j])
        #sum the remaining ints in list\
        substring = given.remove(given[i])
        substring = substring.remove(given[j])
        print(substring)
        #if sum exsists in given list,
        #return sum
    
    
