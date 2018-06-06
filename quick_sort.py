# Quick Sort
# Author: Yusuf Tatlier

#Steps behind quicksort algorithm
# 1. Choose a picot element (reference element)
# 2. Compare the first non-pivot element in the list (index denoted by left_selection) with the last non-pivot element in the list
#    (index denoted by right_selection). 
# 3a. In case left_selection != right_selection, increase left_selection if its value is smaller than the value of the pivot_element  
# 3b. Similary, in case left_selection != right_selection, decrease right_selection if its value is larger than the value of the pivot element
# 3c. When you encounter the situation that value of left_selection is larger than the value of the pivot element and value 
# of the right_selection is smaller than the pivot element, swap the two values. Continue until left_selection = right_selection.
# Perform above steps recursively

def quick_sort(test_list):
    """
    Implementation of the Quick Sort algorithm, which is a recursive algorithm
    """
    
    test_len=len(test_list)
    pivot_index=test_len//2
    pivot = test_list[pivot_index]
    
    if(test_len<2):
        return test_list
    else:
        del test_list[pivot_index]

        left_selection=0
        right_selection=test_len-2
        swap_list=[False,False]

        while(left_selection != right_selection):

            if(test_list[left_selection]>pivot):
                swap_list[0]=True
            else:
                left_selection += 1

            if(test_list[right_selection]<pivot):
                swap_list[1]=True
            else:
                right_selection += -1

            if(sum(swap_list)==2):
                test_list[left_selection], test_list[right_selection] = test_list[right_selection], test_list[left_selection]
                swap_list=[False,False]
        
        if(test_list[left_selection]>pivot):
            sorted_list=test_list[:left_selection]+[pivot]+test_list[left_selection:]
        else:
            sorted_list=test_list[:left_selection+1]+[pivot]+test_list[left_selection+1:]
        
        sorted_list_left=quick_sort(sorted_list[:pivot_index])
        sorted_list_right=quick_sort(sorted_list[pivot_index:])
        return sorted_list_left+sorted_list_right
    
test_list=[15,3,9,8,5,2,7,1,6]
print(quick_sort(test_list))
