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
class Node: #class to represent the object Node
    """
    An object for stroing a single node of a linked list
    Models 2 attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None
    def __init__(self, data): #constructor so class is easy to create
        self.data = data

class Linkedlist: #singly linked list
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data): #new node at head
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def search(self,key):
        """
        search for 1st node if data match key, retrun None if not found
        """
        current = self.head
        while current:
            if current.data == key:
                return current.data
            else:
                current = current.next_node
        return None
    def insert(self,data,index):
        if index == 0:
            self.add(data)
        current = self.head
        new = Node(data)
        pos = index
        for i in range(index-1):
            current = current.next_node
        prev = current
        temp = current.next_node
        
        prev.next_node = new
        new.next_node = temp

    def remove(self,key):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
        return current
        


    def clean_diagram(self):
        my_head = self.head.data
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            if current.next_node == None:
                my_tail = current.data
            current = current.next_node
        print("Head: ",my_head, " and my tail: ",my_tail)
        print(output)
        print(' -> '.join(output))
        
l = Linkedlist()
N1 = Node(10)
l.head = N1
print("My linkedlist size is", l.size())
l.add(3)
l.add(5)
l.add(6)
print("My linkedlist size is", l.size())
l.clean_diagram()
print(l.search(3))
print(l.search(8))
l.insert(2,2)
l.clean_diagram()
l.remove(5)
l.clean_diagram()

    
