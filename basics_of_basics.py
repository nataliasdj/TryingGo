def linear_search(list, target):
    """
    Return index pos of target if found, else return None
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None
def binary_search(list, target):
    l,r = 0, len(list)-1
    while l <= r:
        mid = (r+l)//2 #round down to nearest whole number
        if list[mid] < target:
            l = mid + 1
        elif list[mid] > target:
            r = mid - 1
        elif list[mid] == target:
            return mid
    return None
    
def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        mid = len(list)//2
        
        if list[mid] == target:
            return True
        elif list[mid] > target:
            return recursive_binary_search(list[:mid], target)
        elif list[mid] < target:
            return recursive_binary_search(list[mid+1:], target)
            
        #ask yourself why its not mid-1
    
    
        #answer: bcs [:mid] has already not used that mid index aka, already not included. if you do [mid:] it is still included - it's the slicing pay attention
    
def test(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found")
test(linear_search([1,2,3,4,5],5))
test(binary_search([1,2,3,4,5],4))



#will be creating a node - linked list style


    
