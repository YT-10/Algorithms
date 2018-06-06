# Mergesort
# Author: Yusuf Tatlier

# Steps behind merge-sort algorithm
# 1. Split list until you have lists of length 1
# 2. merge lists through comparison
# 2a. Single element lists: If list1=[a], list2=[b] with a<b --> merge(list1,list2)=[a,b]
# 2b. Multiple element lists: If list1=[a_1,a_2,...,a_n] and list2=[b_1,b_2,...,b_m] , pairwise merging works as
#both lists are already sorted


def merge_sort(test_list):
    """
    Sorting a list using the merge-sort algorithm, which is a recursive algorithm
    """
    
    test_len=len(test_list)
    mid=test_len//2
    
    if(test_len<2):
        return test_list
    else:
        left_test_list=merge_sort(test_list[:mid])
        right_test_list=merge_sort(test_list[mid:])
    merged_list=merge(left_test_list,right_test_list)
    return merged_list

def merge(list1,list2):
    """
    Merging two given lists in increasing order
    """
    total_list=[]
    
    while(len(list1)>0 and len(list2)>0):
        if(list1[0]>list2[0]):
            total_list.append(list2[0])
            del list2[0]
        else:
            total_list.append(list1[0])
            del list1[0]
    return total_list+list1+list2

test_list=[8,1,4,6,2,9,5,5,2,10]
print(merge_sort(test_list))
