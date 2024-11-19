import pygame
import random

pygame.init()

gridWidth = 20
gridHeight = 16
cellSize = 32
screenWidth = gridWidth * cellSize
screenHeight = gridHeight * cellSize
backgroundColor = (255, 192, 203)
lineColor = (50, 50, 50)
fps = 60

screen = pygame.display.set_mode((screenWidth, screenHeight))

moleImage = pygame.image.load("mole.png")
moleImage = pygame.transform.scale(moleImage, (cellSize, cellSize))

moleX = 0
moleY = 0

def drawGrid():
    for x in range(0, screenWidth, cellSize):
        pygame.draw.line(screen, lineColor, (x, 0), (x, screenHeight))
    for y in range(0, screenHeight, cellSize):
        pygame.draw.line(screen, lineColor, (0, y), (screenWidth, y))

def moveMole():
    global moleX, moleY
    moleX = random.randint(0, gridWidth - 1) * cellSize
    moleY = random.randint(0, gridHeight - 1) * cellSize

def drawMole():
    screen.blit(moleImage, moleImage.get_rect(topleft=(moleX, moleY)))

def moleClicked(pos):
    x, y = pos
    return moleX <= x < moleX + cellSize and moleY <= y < moleY + cellSize

def main():
    global moleX, moleY
    clock = pygame.time.Clock()
    running = True
    moleX = 0
    moleY = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if moleClicked(event.pos):
                    moveMole()

        screen.fill(backgroundColor)
        drawGrid()
        drawMole()
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()