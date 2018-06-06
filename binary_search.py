# Binary Search
# Author: Yusuf Tatlier

#Steps behind binary search
#0. It is important to note that the binary search requires a sorted list
#1. Take the middle value of the list and if it is not not equal to the search_value, look at left or right sub-list
#2. Repeat step 1 on the left or right sub-list, until the value is found

def binary_search(test_list,search_value):
    """
    Implementation of the binary search algorithm
    """
    index=0
    test_len=len(test_list)
    
    while(test_len>1):
        mid=test_len//2
        if(test_list[mid]==search_value):
            index += mid
            break
        if(test_list[mid]<search_value):
            test_list=test_list[mid:]
            index += mid
        else:
            test_list=test_list[:mid]
        test_len=len(test_list)
    
    return index

test_list=[7, 8, 10, 45, 50, 52, 63, 72, 90, 100]
binary_search(test_list,63)
print(binary_search(test_list,63))

def binary_search_recursion(test_list,search_value,index=0):
    """
    Implementation of the recursive binary search algorithm
    """
    
    length=len(test_list)
    m=length//2
    
    if(test_list[m]==search_value):        
        return index+m
    else:
        
        if(test_list[m]<search_value):
            index +=m
            return binary_search_recursion(test_list[m:],search_value,index)
        else:
            return binary_search_recursion(test_list[:m],search_value,index)

test_list=[7, 8, 10, 45, 50, 52, 63, 72, 90, 100]
binary_search_recursion(test_list,63)


