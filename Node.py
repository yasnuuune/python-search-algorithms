class Node():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.next = None

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



