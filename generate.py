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
    nodes = []
    # divide screen into a 4x3 grid of zones
    cols, rows = 4, 3
    x_start, y_start = 250, 100
    zone_w, zone_h = 280, 220  # size of each zone

    for i in range(12):
        col = i % cols
        row = i // cols
        # place node randomly WITHIN its zone
        x = x_start + col * zone_w + random.randint(20, zone_w - 20)
        y = y_start + row * zone_h + random.randint(20, zone_h - 20)
        node = Node(x, y, i)
        nodes.append(node)
    return nodes
def generate_edges(nodes):
    edges = []
    edge_counts = {node: 0 for node in nodes}
    max_edges = 3
    max_distance = 450

    for node in nodes:
        others = sorted(
            [n for n in nodes if n != node],
            key=lambda n: (n.x - node.x)**2 + (n.y - node.y)**2
        )
        for target in others:
            dist = ((target.x - node.x)**2 + (target.y - node.y)**2) ** 0.5
            if dist > max_distance:
                break
            if (node, target) in edges or (target, node) in edges:
                continue
            if edge_counts[node] >= max_edges or edge_counts[target] >= max_edges:
                continue
            if random.random() < 0.5:  # 50% chance to skip — adds variety
                continue
            edges.append((node, target))
            edge_counts[node] += 1
            edge_counts[target] += 1

    # make sure every node has at least 1 edge
    for node in nodes:
        if edge_counts[node] == 0:
            others = sorted(
                [n for n in nodes if n != node],
                key=lambda n: (n.x - node.x)**2 + (n.y - node.y)**2
            )
            target = others[0]
            edges.append((node, target))
            edge_counts[node] += 1
            edge_counts[target] += 1

    return edges