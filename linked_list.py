class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self,head = None):
        self.head = head

    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    def show(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def insert(self,new_element,position):
        current = self.head
        if position == 1:
            new_element.next = current
            self.head = new_element
        else:
            count = 1
            while current and count < position - 1:
                current = current.next
                count += 1
            new_element.next = current.next
            current.next = new_element
    def delete(self,val):
        current = self.head
        previous = None
        while current and current.value != val:
            previous = current
            current = current.next
        if current.value == val:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
        

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(Node(5))
ll.show()
print()
ll.insert(Node(6),1)
ll.insert(Node(7),5)
ll.show()

ll.delete(2)
print()
ll.show()
