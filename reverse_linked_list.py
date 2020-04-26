class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self, head = None):
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

    def reverse(self):
        current = self.head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(5)
n5 = Node(7)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.append(n5)
ll.showList()
print()
ll.reverse()
ll.showList()



