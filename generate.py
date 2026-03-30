import random
from Node import Node,LinkedList
import pygame
def generate_tree():
    nodes=12
    tree=LinkedList()
    for i in range(12):
        print("node",i,"generated")
        x,y=generate_pos(tree)
        node=Node(x,y)
        tree.append(node)
        


    return tree



def generate_pos(tree):
    print("im generating position")

    x=random.randint(200,1100)
    y=random.randint(200,1100)
    
    while not tree.compare_x(x) or not tree.compare_y(y):
        x = random.randint(300, 900)
        y = random.randint(200, 600)
    print("position generated")
    return x,y

    
