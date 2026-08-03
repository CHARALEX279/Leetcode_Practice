charges = [5,2,3,1,6]

def find_sum(charges):
    #initial method:
    for i in range(len(charges)):
        for j in range(i+1,len(charges)):
            sub_list = []
            for k in range(len(charges)):
                if charges[k] != charges[i] and charges[k]!= charges[j]:
                    sub_list.append(charges[k])
                    #print(sub_list)
            sub_list_sum = sum(sub_list)
            #print(sub_list_sum)
            if sub_list_sum == charges[i] or sub_list_sum == charges[j]:
                return sub_list_sum

#round two? try subtracting from the total sum
def optimized_find_sum(charges):
    list_sum = sum(charges)
    for i in range(len(charges)):
        for j in range(i+1, len(charges)):
            remainder_total = list_sum - (charges[i] + charges[j])
            if remainder_total == charges[i] or remainder_total == charges[j]:
                return remainder_total

# def ai_assisted_optimized_find_sum(charges):
#     list_sum = sum(charges)
#     for i in range(len(charges)):
#         for j in range(i+1, len(charges)):
#             remainder_total = list_sum - (charges[i] + charges[j])
#             if remainder_total in (charges[i], charges[j]):
#                 return remainder_total

# sum_res=find_sum(charges)
sum_res=optimized_find_sum(charges)
print(sum_res)
