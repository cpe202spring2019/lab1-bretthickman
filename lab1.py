
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    largest = int_list[0]
    for i in int_list:
        if i > largest:
            largest = i
    return largest

def reverse_rec(int_list):   # must use recursion
    if int_list == None:
        raise ValueError
    elif len(int_list) <= 1:
        return int_list
    
    return [int_list[-1]] + reverse_rec(int_list[:-1])        

def bin_search(target, low, high, int_list):  # must use recursion
    if int_list == None:
        raise ValueError
    mid = (high + low) // 2
    high = len(int_list) - 1
    if high + 1 == low:
        return None
    if mid < 0:
        return None
    elif int_list[mid] < target:
        return bin_search(target, mid + 1, high, int_list)
    elif int_list[mid] > target:
        return bin_search(target, low, mid - 1, int_list)
    else:
        return int_list[mid] 
