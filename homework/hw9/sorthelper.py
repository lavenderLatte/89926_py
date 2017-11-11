
def sortNumbers(num_list):
    """
    Sorting numbers in a list in ascending order.
    """       
    int_converted = []
    sorted_list = []

    for i in range(1, len(num_list)): #  eliminating first element since sys.argv is the file name
        int_converted.append(int(num_list[i]))
    print(int_converted)
        
    original_len = len(int_converted) # doesn't get affected the change of int_converted list size
        
    while len(sorted_list) < original_len:  
        sorted_list.append(int_converted.pop(int_converted.index(min(int_converted)))) 
        
    return sorted_list