from basics_of_basics import Linkedlist


def merge(left,right): #the actual merge sorting them in process
    arr = []
    i,j=0,0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    while i < len(left):
        arr.append(left[i])
        i+=1
    while j < len(right):
        arr.append(right[j])
        j+=1
    return arr

def merge_sort(arr_list):
    #return new sorted list
    """
    3 main steps
    1. divide at midpoint and divide into sublist
    2. recursively sort the sublist from step 1
    3, merge the sorted sublist
    """
    if len(arr_list) <= 1:
        return arr_list
    l,r = 0, len(arr_list)-1
    m = len(arr_list) //2
    left_side = merge_sort(arr_list[:m])
    right_side = merge_sort(arr_list[m:])
    return merge(left_side,right_side)

test_list = [1,9,6,3,6,4,5,8,2]
print("this is output: ", merge_sort(test_list))