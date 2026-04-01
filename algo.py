import pygame
from Node import Node,LinkedList
from functions import dijikstra,get_distance
from generate import generate_nodes, generate_edges
import random
pygame.init()
state="menu"
selecting="start"
screen=pygame.display.set_mode((1500,900))
running=True
font = pygame.font.Font('freesansbold.ttf', 32)

FPS = pygame.time.Clock()

list=["bfs","dfs","a*","dijikstra"]
rect1= pygame.Rect(50,90,80,40)
rect2=pygame.Rect(50,140,80,40)
rect3=pygame.Rect(50,190,80,40)
rect4=pygame.Rect(50,240,80,40)

start_node=None
target_node=None
tree=None
edges = []
dijikstra=False
while running:
    screen.fill('purple' )
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if state == "menu":
                    if rect1.collidepoint(event.pos):
                        tree = generate_nodes()
                        edges = generate_edges(tree)
                        state = "selecting"
                        print("bfs")
                        bfs=True
                    elif rect2.collidepoint(event.pos):
                        tree = generate_nodes()
                        edges = generate_edges(tree) 
                        state = "selecting"
                        print("dfs")
                        dfs=True
                    elif rect3.collidepoint(event.pos):
                        tree = generate_nodes()
                        edges = generate_edges(tree)
                        state = "selecting"
                        print("astar")
                        astar=True
                    elif rect4.collidepoint(event.pos):
                        tree = generate_nodes()
                        edges = generate_edges(tree)
                        state = "selecting"
                        dijikstra=True

                elif state == "selecting":
                    print("selecting state, clicked at", event.pos)  # ADD THIS
                    for node in tree:
                        dist = ((event.pos[0] - node.x)**2 + (event.pos[1] - node.y)**2) ** 0.5
                        if dist <= 20:
                            print("HIT A NODE")  # ADD THIS
                            if selecting == "start":
                                start_node = node
                                selecting = "target"
                                print("start node set")
                            elif selecting == "target":
                                target_node = node
                                state = "running"
                                print("target node set")
                            break



            


    if edges:
         for node,target in (edges):
            pygame.draw.line(screen, 0, (node.x,node.y), (target.x,target.y)) 
            distance=font.render(str(get_distance(node,target)),True, (255,255,255))
            screen.blit(distance, (((node.x+target.x)/2),(((node.y+target.y)/2))))
    if tree:
        for node in tree:
            if node == start_node:
                color = (0, 255, 0)    # green = start
            elif node == target_node:
                color = (255, 0, 0)    # red = target
            else:
                color = (0, 200, 255)  # blue = default
            pygame.draw.circle(screen, color, (node.x, node.y), 20)


                
                
    if state=="menu": 
    
        page_title  = font.render("Choose the algorithm you want to run:", True, (255, 255, 255))
        screen.blit(page_title, (50, 50))

        pygame.draw.rect(screen,0,rect1)
        pygame.draw.rect(screen,0,rect2)
        pygame.draw.rect(screen,0,rect3)
        pygame.draw.rect(screen,0,rect4)
        text1=font.render(list[0],True,(255, 255, 255))
        text2=font.render(list[1],True,(255, 255, 255))
        text3=font.render(list[2],True,(255, 255, 255))
        text4=font.render(list[3],True,(255, 255, 255))
        text1_rect=text1.get_rect(center=rect1.center)
        text2_rect=text2.get_rect(center=rect2.center)
        text3_rect=text3.get_rect(center=rect3.center)
        text4_rect=text4.get_rect(center=rect4.center)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        screen.blit(text3, text3_rect)
        screen.blit(text4,text4_rect)

    if state == "selecting":
        # draw nodes + hint text
        if selecting == "start":
            hint = font.render("Click a node to set START", True, (255,255,255))
        else:
            hint = font.render("Click a node to set TARGET", True, (255,255,255))
        screen.blit(hint, (50, 50))
        
       

    elif state == "running":
        pass


        

    pygame.display.flip()






pygame.quit()