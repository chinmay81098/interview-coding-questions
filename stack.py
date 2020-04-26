class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self,head= None):
        self.head = head
    def insert_first(self,new_element):
        current = self.head
        self.head = new_element
        new_element.next = current
    def delete_first(self):
        if self.head:
            current = self.head
            self.head = current.next
            return current.value
        else:
            return "Stack Empty"
class Stack(object):
    def __init__(self,top = None):
        self.ll = LinkedList(top)
    def push(self,value):
        self.ll.insert_first(value)
    def pop(self):
        return self.ll.delete_first()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

stack = Stack(n1)

stack.push(n2)
stack.push(n3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.push(Node(4))
stack.push(Node(5))
stack.push(Node(6))
stack.push(Node(7))
print(stack.pop())
print(stack.pop())
