class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList():
    def __init__(self,head = None):
        self.head = head
    
    def append(self,new_element):
        current = self.head
        while current.next:
            current = current.next
        current.next = new_element
    
    def showList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    #Method 1
    def checkLoop(self):
        hash = set()
        current = self.head
        while current:
            if current in hash:
                return "Loop Found"
            else:
                hash.add(current)
            current = current.next
        return "No Loop Found"
    #Method 2 : Floyd's cycle detecting algorithm
    def detectLoop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return "Loop Found"
        return "No Loop Found"

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

ll.showList()
print()
n4.next = n2 # add a loop to verify

print(ll.checkLoop())
print(ll.detectLoop())