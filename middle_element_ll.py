class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,head = None):
        self.head = head
        if self.head:
            self.size = 1
        else:
            self.size = 0

    def append(self,new_element):
        self.size += 1
        current = self.head
        while current.next:
            current = current.next
        current.next = new_element
    def showList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def get_size(self):
        return self.size

    def get_middle_element(self,position):
        current = self.head
        count = 1
        while current and count < position:
            current = current.next
            count += 1
        return current.value

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.append(Node(7))
ll.showList()
print()
size = ll.get_size()
print("Total Size: {}".format(size))
print()
mid = (size + 1)//2
middle_element = ll.get_middle_element(mid)
print("Middle element is: {}".format(middle_element))