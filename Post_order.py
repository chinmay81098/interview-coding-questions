class Node(object):
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def inorder_print(self,start,traversal):
        '''Left->Right->Root'''
        if start:
            traversal =  self.inorder_print(start.left,traversal)
            traversal  = self.inorder_print(start.right,traversal)
            traversal += (str(start.value) + "->")
        return traversal


#set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(3)             
tree.root.left.right = Node(4)                               #                1
tree.root.left.right.left = Node(5)                          #             /      \ 
                                                             #           2         6
tree.root.right = Node(6)                                    #          / \      /   \
tree.root.right.left = Node(7)                               #         3   4    7     8
tree.root.right.right = Node(8)                              #             /       /   \
tree.root.right.right.left = Node(9)                         #            5       9     10
tree.root.right.right.right = Node(10)


print(tree.inorder_print(tree.root,""))