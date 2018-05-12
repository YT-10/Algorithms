#Simple linear search

# Search goes linearly through a list and returns first occurence of search_value

test_list=[10,7,45,100,50,63,52,90,8,72] #Index of 52 is 6

def linear_search(test_list,search_value):
    """
    Performs a simple linear search """
    test_len=len(test_list)
    
    
    for index in range(0,test_len):
        if(test_list[index]==search_value):
            return(index) 
    
    print("List doesn't contain the value")

print(linear_search(test_list,52))