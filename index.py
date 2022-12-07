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

screen = pygame.display.set_mode((screenWidth, screenHeight))

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
    while True:
        screen.fill(background)
        
        snakeX = screenWidth/2
        snakeY = screenHeight/2
        
        foodX = 300
        foodY = 400
        
        gameOver=False
        gamePause=False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('Pause')
                    gamePause=True
       
        while not gameOver:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print('Pause')
                        gamePause=True
                        
            while gamePause:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.display.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gamePause=False
                        elif event.key == pygame.K_q:
                            pygame.display.quit()
                
                pygame.draw.rect(screen, brown, [0, 0, screenWidth*0.8, screenHeight*0.8])
                pygame.display.update()
                
            pygame.draw.rect(screen, violet, [200, 200, 10, 10])
            pygame.draw.rect(screen, brown, [foodX, foodY, 10, 10])
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
     
        pygame.display.update()
    
    
homeScreen()