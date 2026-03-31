class Node():
    def __init__(self,x,y,i):
        self.x = x
        self.y = y
        self.i=i
        self.next = None
class TreeNode:
    def __init__(self):
        self.head=None
        self.children = [] # List to hold child nodes
    
    def add_child(self, TreeNode):
        self.children.append(TreeNode)



class LinkedList():
    def __init__(self):
        self.head=None
    def append(self,node):
        if self.head is None:
            self.head=node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=node
    def display(self):
        current_node=self.head
        while current_node:
            print(current_node.x, '=>')
            current_node=current_node.next
        print('none')
    def compare_x(self,x):
        current_node=self.head
        while current_node:
            if abs(current_node.x-x)<=20:
                return False
            current_node=current_node.next
        return True
    def compare_y(self,y):
        current_node=self.head
        while current_node:
            if abs(current_node.y-y)<=20:
                return False
            current_node=current_node.next
        return True
    def getNodeByIndex(self,i):
        current_node=self.head
        while current_node:
            if current_node.i==i:
                return current_node
            current_node=current_node.next
        return current_node




