import pygame
from constants2 import *
from perceptron2 import *

pygame.init()
weights = WEIGHTS[:]

def draw_pixel(color):
    pygame.draw.rect(screen,color,pygame.Rect((30,30),(30,30)))


def draw_weight_Text(text,x,y):
    W_0 = font.render(text,True,BLACK,)
    W_0_Rect = W_0.get_rect()
    W_0_Rect.center = (x,y)
    screen.blit(W_0,W_0_Rect)

def draw_weight(weights,x,y):
    dy = 0
    for weight in weights:
        W = font.render(str(weight),True,BLACK,)
        W_Rect = W.get_rect()
        W_Rect.center = (x,y+dy)
        dy += 30
        screen.blit(W,W_Rect)

def pixel_color(value):
    if value==1: return 'BRIGHT'
    return 'DARK'

pygame.font.init()
pygame.display.set_caption("PERCEPTRON COLOR")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 16)

text = font.render('PREDICTED VALUE', True, BLACK,)
textRect = text.get_rect()
textRect.center = (200, 30)



iteration = 0
ANIMATING = True
i = 0
error = 0
predicted = 0
while ANIMATING:

    #background
    screen.fill("grey")
    draw_pixel(tuple(EXAMPLES[i][1:]))
    #update the screen
    screen.blit(text, textRect)
    draw_weight_Text("W0 = ",50,100)
    draw_weight_Text("W1 = ",50,130)
    draw_weight_Text("W1 = ",50,160)
    draw_weight_Text("W2 = ",50,190)
    draw_weight_Text('Error =',175,220)
    draw_weight_Text(str(error),225,220)
    draw_weight_Text('Epoch: '+str(iteration+1),150,250)
    draw_weight(weights,100,100)
    if (i==0):
        color = pixel_color(predict(weighted_sum(weights,EXAMPLES[i])))
    else:
        color = pixel_color(predicted)
        
    
    draw_weight_Text(color,200,60)
    if(error ==0 and i ==len(EXAMPLES)-1):
        draw_weight_Text('TRAINING COMPLETE',200,280)
    pygame.display.flip()

    #track user interactions
    for event in pygame.event.get():

        #closing the window
        if event.type == pygame.QUIT:
            ANIMATING = False
        #press some keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ANIMATING = False
            elif event.key == pygame.K_RETURN:
                if (i==len(EXAMPLES)-1):
                    i=0
                    error = 0
                    iteration+=1
                else:
                    i+=1
                s = weighted_sum(weights,EXAMPLES[i])
                predicted = predict(s)
                
                if predicted != OUTPUT[i]:
                    error+=1
                    weights = rectify_weights(weights,predicted,OUTPUT[i],EXAMPLES[i])
                
                