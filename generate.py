import random
from Node import Node,LinkedList,TreeNode
import pygame
def generate_tree():
    nodes = 12
    nb_nodes = 0  # will track number of nodes created

    def create_node():
        nonlocal nb_nodes
        if nb_nodes >= nodes:
            return None

        nb_nodes += 1
        node = TreeNode()
        x = random.randint(0, 3)  # number of children
        for _ in range(x):
            child = create_node()
            if child:
                node.add_child(child)
        return node

    root = create_node()
    return root

def compare(x,nodes):
    for node in nodes:
        if abs(node.x-x)<=30:
            return False
    return True


def generate_pos(nodes,j):

    level_y=[100,200,300,400,500,600,700,800]
    if j<=3:
        y=random.choice(level_y)
        x=random.choice([300,400,500,600])
        return x,y
    if j>=4 and j<=7:
        y=random.choice(level_y)
        x=random.choice([700,800,900,1000])
        return x,y
    if j>7:
        y=random.choice(level_y)
        x=random.choice([1100,1200,1300])
        return x,y
        
     


def generate_nodes():
    nodes=[]
    for i in range(12):
        x,y=generate_pos(nodes,i)
        node=Node(x,y,i)
        nodes.append(node)
    return nodes

def generate_edges(nodes):
    edges=[]
    for node in nodes:
        x=random.randint(1,3)
        for i in range(x):
            target=random.choice(nodes)
            if target!=node and (target,node)not in edges and (node, target)not in edges and edges.count(target)<=3 and edges.count(node)<=3:
                edges.append((node,target))

    return edges