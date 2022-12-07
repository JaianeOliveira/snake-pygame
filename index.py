import random

import pygame
from pygame.locals import *

pygame.init()

screenWidth=800
screenHeight=600

violet=(106, 0, 228)
white=(225, 255, 255)
brown=(170, 139, 86)
greenPrimary=(57, 81, 68)
greenSecondary=(78, 108, 80)
red = (255, 0, 0)
background=(34, 30, 37)
green=(78, 188, 91)
menu=(54, 50, 60)

screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

titleFont = pygame.font.Font('./PressStart2P-Regular.ttf', 20)
font = pygame.font.Font('./CourierPrime-Regular.ttf', 16)

snakeSpeed=30

def generateSnake(snake, snakeBlock = 10, color=violet):
    for x in snake:
        pygame.draw.rect(screen, color, [x[0], x[1], snakeBlock, snakeBlock])


def writeTitle(message, color=white, fontSize=20):
    font = pygame.font.Font('./PressStart2P-Regular.ttf', fontSize)
    return font.render(message, True, color)
def writeText(message, color=white, fontSize=16):
    font = pygame.font.Font('./CourierPrime-Regular.ttf', fontSize)
    return font.render(message, True, color)

def pauseMenu(gamePause):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
                    
        screen.fill(background)
        
        pygame.display.update()
        
def gameLoop():
    gameClose=False
    while True:
        screen.fill(background)
        
        snakeX = screenWidth/2
        snakeY = screenHeight/2
        
        snakeXChange = 0       
        snakeYChange = 0
        
        snakeBody=[]
        snakeLength=1
        
        foodX=round(random.randrange(0, screenWidth - 10) / 10.0) * 10.0
        foodY=round(random.randrange(0, screenHeight - 10) / 10.0) * 10.0
        
        gamePause=False
        gameOver=False
        gameOverCause=''
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                exit()
       

        while not gameClose:
            screen.fill(background)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not gameOver:
                        gamePause= not gamePause
                    elif event.key == pygame.K_q and (gamePause or gameOver):
                        gameClose=True
                        homeScreen()
                       
                    elif event.key == pygame.K_n and (gameOver or gamePause):
                        gameLoop()

                    elif event.key == pygame.K_LEFT:
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
                    
                        
            if gamePause:
                pygame.draw.rect(screen, menu, [screenWidth*0.1, screenHeight*0.1, screenWidth*0.8, screenHeight*0.8], 400, 8)
                screen.blit(writeTitle("Jogo Pausado"), [screenWidth/2 - 115, screenHeight*0.15])
                screen.blit(writeText("Pressione [Esc] para continuar ou [Q] para sair"), [screenWidth/2 - 220, screenHeight*0.85])
            elif gameOver:
                pygame.draw.rect(screen, menu, [screenWidth*0.1, screenHeight*0.1, screenWidth*0.8, screenHeight*0.8], 400, 8)
                screen.blit(writeTitle("Game Over", red), [screenWidth/2 - 88, screenHeight*0.4])
                screen.blit(writeText(gameOverCause), [screenWidth/2 - len(gameOverCause)*5, screenHeight*0.50])
                screen.blit(writeText("Pressione [N] para um novo jogo ou [Q] para sair"), [screenWidth/2 - 220, screenHeight*0.85])

            else:
                if snakeX >= screenWidth or snakeX < 0 or snakeY >= screenHeight or snakeY < 0:
                    gameOver = True
                    gameOverCause='Você bateu na parede'
                    
                snakeX += snakeXChange
                snakeY += snakeYChange
                
                screen.fill(background)
                    
                food = pygame.draw.rect(screen, brown, [foodX, foodY, 10, 10])
                
                snakeHead=[]
                snakeHead.append(snakeX)
                snakeHead.append(snakeY)
                snakeBody.append(snakeHead)
                
                if len(snakeBody) > snakeLength:
                    del snakeBody[0]
                    
                for x in snakeBody[:-1]:
                    if x == snakeHead:
                        gameOver=True
                        gameOverCause='Você mordeu sua própria cauda'
                
                if int(snakeX) == int(foodX) and int(snakeY) == int(foodY):
                    foodX=round(random.randrange(0, screenWidth - 10) / 10.0) * 10.0
                    foodY=round(random.randrange(0, screenHeight - 10) / 10.0) * 10.0

                    snakeLength += 1
                
                generateSnake(snakeBody)
                
            clock.tick(snakeSpeed)
            pygame.display.update()
        
        if gameClose:
            break
        pygame.display.update()


    

def homeScreen():
    while True:
        screen.fill(background)
 
        startGame = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('Pause')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                startGame=True
     
        if startGame:
            print('começou')
            gameLoop()
        else:
            screen.blit(writeTitle("Snake", white, 30), [screenWidth*0.4, screenHeight*0.3])
            pygame.draw.polygon(screen, green, [(screenWidth/2 - 25, screenHeight/2), (screenWidth/2 - 25, screenHeight/2 + 50), (screenWidth/2 + 25, screenHeight/2 + 25)])
            screen.blit(writeText("Pressione qualquer lugar para iniciar", white, 20), [screenWidth*0.23, screenHeight*0.7])
     
        pygame.display.update()
    
    
homeScreen()