#Bubble sort 

#Steps behind bubblesort algorithm:
# 1. Go linearly through a list with length n and compare neighbors (n-1 comparisons) 
# 2. Swap neighbors if left value is higher than right value, during each of the (n-1) steps
# After (n-1) steps, the highest value is definitely placed at the end of the list 
# 3. Repeat this step for the sub-list of (n-1) elements etc.
# This procedure guarantees that the list becomes ordered. 

def bubble_search(test_list):
    """
    Implementation of the bubble search algorithm
    """
  
    test_len=len(test_list)
    
    while(test_len>0):
        for guide_index in range(test_len-1):
            if(test_list[guide_index]>test_list[guide_index+1]):
                test_list[guide_index], test_list[guide_index+1] = test_list[guide_index+1], test_list[guide_index]
        test_len += -1

    return test_list

def bubble_search_recursive(test_list,search_range):
    """
    Recursive bubble search algorithm
    """
    
    
    if(search_range<2):
        return test_list
    else:
        for guide_index in range(search_range-1):
            if(test_list[guide_index]>test_list[guide_index+1]):
                test_list[guide_index], test_list[guide_index+1] = test_list[guide_index+1], test_list[guide_index]
        return bubble_search_recursive(test_list,search_range-1)

        
test_list=[6,5,3,1,8,2,4,7]
length=len(test_list)

print(bubble_search(test_list))
print(bubble_search_recursive(test_list,length))
