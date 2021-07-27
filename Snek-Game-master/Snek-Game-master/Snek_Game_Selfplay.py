# Python Snek Game 
import pygame
import random
import time
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

#PYGAME VARIABLES
width=500
height=500

#COLORS
white=(255,255,255)
black=(0,0,0)
greeen=(0,255,0)
red=(255,0,0)

pygame.init()
info = pygame.display.Info()
width=info.current_w
height=info.current_h

window = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
clock = pygame.time.Clock()
font_style = pygame.font.SysFont('monospace',30)
score_font = pygame.font.SysFont('monospace',25)
pygame.display.update()

def rand_food_spawn():
    global food_x
    global food_y
    food_x=random.randrange(20,width-20,20)
    food_y=random.randrange(20,height-20,20)
    
def draw_snake(snake_Head,snake_body):
    for body in snake_body:
        pygame.draw.rect(window,white,[body[0],body[1],snake_Head,snake_Head])
        
high_score = 0
def show_score():
    global high_score
    if length_snake>high_score: high_score=length_snake
    sco = score_font.render(f'LENGTH : {length_snake}    HIGH SCORE : {high_score}',True,greeen)
    window.blit(sco,[0,0])
    


    
def play_game():
    a='X'
    # Food Variables
    global food_x
    global food_y
    
    food_x=random.randrange(20,width-20,20)
    food_y=random.randrange(20,height-20,20)
    
    #SNAKE VARIABLES
    direction='STOP'
    snake_head_size=18

    x_move=0
    y_move=0

    x_pos=width/2
    y_pos=height/2

    speed=20

    snake_body=[]
    global length_snake
    length_snake=1
    
    Running=True
    while Running:
        window.fill(black)
        
        # Pygame events
        for event in pygame.event.get():
            # Check for exit
            if event.type == pygame.QUIT:
                exit()

            
            # Check for keypresses and move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    exit()
                
                    
        # Check if out of boundary
        if x_pos<0 or x_pos>width or y_pos<0 or y_pos>height:
            print('>>> OUT OF BOUNDARY')
            play_game()
        
        # Check if head collided with food
        if x_pos == food_x and y_pos ==  food_y:
            print('>>> ATE FOOD')
            length_snake+=1
            rand_food_spawn()
            
        x_pos += x_move
        y_pos += y_move
        
        # Make the snake body
        snake_head=[]
        snake_head.append(x_pos)
        snake_head.append(y_pos)
        snake_body.append(snake_head)

        # Auto move
        
        if a=='X':
            a='Y'
            if x_pos < food_x and direction != 'LEFT':
                x_move=speed
                y_move=0
            if x_pos > food_x and direction != 'RIGHT':
                x_move=-speed
                y_move=0
            
        if a=='Y':
            a='X'
            #if x_pos == food_x:
                
            if y_pos < food_y and direction != 'UP':
                x_move=0
                y_move=speed
                                
            if y_pos > food_y and direction != 'DOWN':
                x_move=0
                y_move=-speed
        
        if len(snake_body) > length_snake:
            del snake_body[0]
            
        # Check collisions with the body
        for body in snake_body[:-1]:
            if body == snake_head :
                print('>>> ATE YOURSELF')
                play_game()
                
        
                
        draw_snake(snake_head_size,snake_body)
        pygame.draw.rect(window,red,[food_x,food_y,20,17])#draws food
        show_score()# displays the score
        pygame.display.update()
        
        clock.tick(30)

play_game()
    
pygame.quit()
quit()
