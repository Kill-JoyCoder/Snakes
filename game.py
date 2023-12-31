import pygame
import time
import random 

pygame.init()
"""
pygame.mixer.music.load("blue.mp3")
pygame.mixer.music.set_volume(0.20)
pygame.mixer.music.play(loops=2, fade_ms=5000)
"""

white = (255,255,255)
red   = (220,0,50)
blue  = (0,0,255)
black = (0,0,0)

dw=600
dh=400

dis = pygame.display.set_mode((dw,dh))
pygame.display.set_caption('Snakes!')

clock = pygame.time.Clock()

snake_block=10
snake_speed=15

font_style = pygame.font.SysFont('sans', 25)
score_font = pygame.font.SysFont('comicsansms', 35)



def message(msg, colour):
    mesg=font_style.render(msg, True, colour)
    dis.blit(mesg ,[dw/3,dh/3])


def gameloop():
    g_over=False
    g_close=False
    
    x=dw//2
    y=dh//2
    
    x_change=0
    y_change=0
    
    snake_list =[]
    length=1

    foodx = round(random.randrange(0, dw/2-snake_block)/10.0)*10.0
    foody = round(random.randrange(0, dh/2-snake_block)/10.0)*10.0
    
    while not g_over:
        
        while g_close == True:
            dis.fill(black)
            message("Q-quit,C-play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        g_over = True
                        g_close = False 
                    if event.key == pygame.K_c:
                        gameloop()
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                g_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
        if x>=dw or x<0 or y>=dh or y<0 :
          g_close = True
          
        x += x_change
        y += y_change

        dis.fill(black)
        pygame.draw.rect(dis, white, [foodx,foody, snake_block, snake_block])
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
              
        if x==foodx and y==foody:
            foodx = round(random.randrange(0, dw-snake_block)/10.0)*10.0
            foody = round(random.randrange(0, dh-snake_block)/10.0)*10.0
            length +=1 
        if len(snake_list) > length:
            del snake_list[0]
        
        for i in snake_list[:-1]:
            if i == snake_head:
                g_close = True
        
        snake(snake_block, snake_head)  
        pygame.display.update()
        
        #food and changes
        
            
        clock.tick(snake_speed)
def snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, blue,[i[i],i[1],snake_block,snake_block])
        print("!!")
    
    pygame.quit()
    quit()

gameloop()