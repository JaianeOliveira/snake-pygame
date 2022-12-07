import random
import time

import pygame

# colors
violet=(106, 0, 228)
white=(225, 255, 255)
brown=(170, 139, 86)
greenPrimary=(57, 81, 68)
greenSecondary=(78, 108, 80)
red = (255, 0, 0)
background=(34, 30, 37)

# screen sizes
screenWidth=800
screenHeight=600

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Snake')

snakeBlock=10
snakeSpeed=30
score=0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def showScore(score):
    value = score_font.render("Score: " + str(score), True, brown)
    screen.blit(value, [0, 0])

def generateSnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(screen, violet, [x[0], x[1], snakeBlock, snakeBlock])

def message(msg, color):
    write = font_style.render(msg, True, color)
    screen.blit(write, [screenWidth/2, screenWidth/2])
    
def initialScreen():
    while True:
        screen.fill(background)
        pygame.draw.rect(screen, white, [10, 10, 100, 50])
        pygame.display.update()

def gameLoop():
    gameOver=False
    gameClose=False
    gamePause=False
    snakeX = screenWidth/2
    snakeY = screenHeight/2
   
    snakeXChange = 0       
    snakeYChange = 0
    
    snakeList=[]
    snakeLength=1
  
    foodX=round(random.randrange(0, screenWidth - snakeBlock) / 10.0) * 10.0
    foodY=round(random.randrange(0, screenHeight - snakeBlock) / 10.0) * 10.0

    while not gameOver:
        while gameClose:
            screen.fill(background)
            message("Pessione Q ou C", violet)
            showScore(snakeLength - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver=True
                        gameClose=False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver=True
                exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snakeXChange = -10
                    snakeYChange = 0
                elif event.key == pygame.K_RIGHT:
                    snakeXChange = 10
                    snakeYChange = 0
                elif event.key == pygame.K_UP:
                    snakeYChange = -10
                    snakeXChange = 0
                elif event.key == pygame.K_DOWN:
                    snakeYChange = 10
                    snakeXChange = 0
                elif event.key == pygame.K_ESCAPE:
                    gameOver=True
            
            

        
        if snakeX >= screenWidth or snakeX < 0 or snakeY >= screenHeight or snakeY < 0:
            gameClose = True

        snakeX += snakeXChange
        snakeY += snakeYChange
        
        screen.fill(background)               
        
        # desenha a comida
        pygame.draw.rect(screen, greenSecondary, [foodX, foodY, snakeBlock, snakeBlock])
        
        snakeHead=[]
        snakeHead.append(snakeX)
        snakeHead.append(snakeY)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose=True
        
        generateSnake(snakeBlock, snakeList)
        showScore(snakeLength - 1)
        
        pygame.display.update()
        
        if int(snakeX) == int(foodX) and int(snakeY) == int(foodY):
            foodX=round(random.randrange(0, screenWidth - snakeBlock) / 10.0) * 10.0
            foodY=round(random.randrange(0, screenHeight - snakeBlock) / 10.0) * 10.0
            snakeLength += 1
        
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()

initialScreen()