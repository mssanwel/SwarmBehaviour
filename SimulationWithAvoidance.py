import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))


class bird:
    def __init__(self):
        self.originalImage = pygame.image.load("bird.png")
        self.birdImage = pygame.image.load("bird.png")
        self.birdWidth = 10
        self.birdHeight = 20
        self.birdImage = pygame.transform.scale(self.birdImage, (self.birdWidth, self.birdHeight))
        self.originalImage = pygame.transform.scale(self.originalImage, (self.birdWidth, self.birdHeight))
        self.bX = random.randint(0, 790)
        self.bY = random.randint(0, 580)
        self.degrees = random.randint(0,359)
        self.radian = math.radians(self.degrees)  # measured from positive x-axis
        #self.birdImage = pygame.transform.rotate(self.birdImage, self.degrees - 90)
        self.vX = 0.5 * math.cos(self.radian)
        self.vY = 0.5 * math.sin(self.radian)

    def updateOrientation(self):

        angle=math.degrees(math.atan(self.vY/self.vX))
        self.birdImage = pygame.transform.rotate(self.originalImage, angle-270)
        #print(angle+90)
        self.bX += self.vX
        self.bY += self.vY
        if self.bX >= 800:
            self.bX = 0
        if self.bY >= 600:
            self.bY = 0
        if self.bX < 0:
            self.bX = 800
        if self.bY < 0:
            self.bY = 600
        screen.blit(self.birdImage, (self.bX, self.bY))


running = True
c = 0
n=5
b = [bird() for i in range(n)]
while (running):
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    c += 1
    # delay to add reaction time of system
    if c % 30 == 0:
        # Swarm rules
        # finds closest bird
        # Aligns its direction with closest bird
        for i in range(n):
            min = 1000
            index = -1
            xDiff = 0
            yDiff = 0
            lRate = 1.2
            for j in range(n):
                if (i!=j):
                    if ((b[i].vX * b[j].vX) + (b[i].vY * b[j].vY)) > 0:
                        if (pow((pow((b[i].bX - b[j].bX), 2) + pow((b[i].bY - b[j].bY), 2)), 1/2) < min):
                            index=j
                            min=pow((pow((b[i].bX - b[j].bX), 2) + pow((b[i].bY - b[j].bY), 2)), 1/2)

            xDiff = b[index].vX - b[i].vX
            yDiff = b[index].vY - b[i].vY
            b[i].vX += lRate * xDiff
            b[i].vY += lRate * yDiff

    for i in range(n):
        b[i].updateOrientation()

    pygame.display.update()
