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

    def get_middle_element(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.value

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)

ll.showList()
print()
middle_element = ll.get_middle_element()
print("Middle element is: {}".format(middle_element))