class Queue():
    def __init__(self,head = None):
        self.storage = [head]
    def enqueue(self,element):
        self.storage.append(element)
    def dequeue(self):
        return self.storage.pop(0)
    def peek(self):
        return self.storage[0]

q = Queue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.peek())