from Node import LinkedList
def dijikstra(screen, font, nodes,edges,start_node,target_node):
    curr=start_node
    explored=[curr]
    path=LinkedList()
    l={"distance","node"}
    while curr!=target_node:
        neighbor_nodes=neighbors(curr,nodes,edges)
        

        for node in neighbor_nodes:
            distance=get_distance(curr,node)
            l.a=node
            l.b=curr
            l.d=distance
        min_node=get_min_node(l)
        explored.append(min_node)
        curr=min_node




def neighbors(start_node,nodes,edges):
    neighbor_nodes=set()
    for node,target in nodes:
        if node==start_node:
            neighbor_nodes.add(target)
        elif node==target:
            neighbor_nodes.add(node)
    return neighbor_nodes

def get_distance(node1,node2):
    return abs(((node1.x-node2.x)**2)+((node1.y-node2.y))**2)

def get_min_node(list):
    min_d=list[0].d
    min_n=list[0]
    for i in list:
        if i.d<min_d:
            min_d=i.d
            min_n=i
    return min_n
