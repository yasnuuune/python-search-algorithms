import pygame
from Node import Node,LinkedList
#from functions import dfs,bfs,astar,dijikstra
from generate import generate_tree
pygame.init()
screen=pygame.display.set_mode((1500,900))
running=True
font = pygame.font.Font('freesansbold.ttf', 32)

FPS = pygame.time.Clock()
circles=[
    {"y":200,"x":300, "r":20},
    {"y":200,"x":400, "r":20},
    {"y":200,"x":500, "r":20},
    {"y":200,"x":600, "r":20},
    {"y":200,"x":700, "r":20},
    {"y":200,"x":800, "r":20},
    {"y":200,"x":900, "r":20},
        {"y":300,"x":300, "r":20},
    {"y":300,"x":400, "r":20},
    {"y":300,"x":500, "r":20},
    {"y":300,"x":600, "r":20},
    {"y":300,"x":700, "r":20},
    {"y":300,"x":800, "r":20},
    {"y":300,"x":900, "r":20},
        {"y":400,"x":300, "r":20},
    {"y":400,"x":400, "r":20},
    {"y":400,"x":500, "r":20},
    {"y":400,"x":600, "r":20},
    {"y":400,"x":700, "r":20},
    {"y":400,"x":800, "r":20},
    {"y":400,"x":900, "r":20},
        {"y":500,"x":300, "r":20},
    {"y":500,"x":400, "r":20},
    {"y":500,"x":500, "r":20},
    {"y":500,"x":600, "r":20},
    {"y":500,"x":700, "r":20},
    {"y":500,"x":800, "r":20},
    {"y":500,"x":900, "r":20},
        {"y":600,"x":300, "r":20},
    {"y":600,"x":400, "r":20},
    {"y":600,"x":500, "r":20},
    {"y":600,"x":600, "r":20},
    {"y":600,"x":700, "r":20},
    {"y":600,"x":800, "r":20},
    {"y":600,"x":900, "r":20},






]
list=["bfs","dfs","a*","dijikstra"]
rect1= pygame.Rect(50,90,80,40)
rect2=pygame.Rect(50,140,80,40)
rect3=pygame.Rect(50,190,80,40)
rect4=pygame.Rect(50,240,80,40)
tree=None
dijikstra=False
while running:
    screen.fill('purple')
    mouse_pos=pygame.mouse.get_pos()
    mouse_pressed=pygame.mouse.get_pressed()
    for event in pygame.event.get():
        print(event)  # add this, it will print EVERY event
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                if rect1.collidepoint(mouse_pos):
                        #bfs()
                        print("bfs")
                elif rect2.collidepoint(mouse_pos):
                        #dfs()
                        print("dfs")
                elif rect3.collidepoint(mouse_pos):

                        #astar()
                        print("astar")
                elif rect4.collidepoint(mouse_pos):

                        print("dijikstra clicked")
                        #dijikstra()
                        print("dijikstra")
                        dijikstra=True
                        tree=generate_tree()
                        print("tree generated")



            

    if tree:
        curr_node = tree.head
        while curr_node:
            print(f"node at {curr_node.x}, {curr_node.y}")
            pygame.draw.circle(screen, (0, 200, 255), (curr_node.x, curr_node.y), 20)
            curr_node = curr_node.next

    page_title = font.render("Choose the algorithm you want to run:", True, (255, 255, 255))
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
    

    
    
        


    

    pygame.display.flip()






pygame.quit()