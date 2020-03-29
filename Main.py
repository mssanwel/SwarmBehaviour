import pygame
import math
import random
pygame.init()
screen=pygame.display.set_mode((800,600))

class bird:
    def __init__(self):
        self.originalImage = pygame.image.load("bird.png")
        self.birdImage = pygame.image.load("bird.png")
        self.birdWidth=10
        self.birdHeight=20
        self.birdImage=pygame.transform.scale(self.birdImage,(self.birdWidth,self.birdHeight))
        self.originalImage = pygame.transform.scale(self.originalImage, (self.birdWidth, self.birdHeight))
        self.bX = random.randint(0,790)
        self.bY = random.randint(0,580)
        self.vX=0
        self.vY=0
        self.degrees = 45 + 90
        self.radian = math.radians(self.degrees)  # measured from positive x-axis
        self.birdImage = pygame.transform.rotate(self.birdImage, self.degrees - 90)
        self.vX = 0.5 * math.cos(self.radian)
        self.vY = 0.5 * math.sin(self.radian)

    def updateOrientation(self, angle):
        self.degrees = angle
        self.radian = math.radians(self.degrees)  # measured from positive x-axis
        self.birdImage = pygame.transform.rotate(self.originalImage, self.degrees - 90)
        self.vX = 0.5 * math.cos(self.radian)
        self.vY = 0.5 * math.sin(self.radian)
        self.bX += self.vX
        self.bY -= self.vY
        if self.bX>=800:
            self.bX=0
        if self.bY>=600:
            self.bY=0
        if self.bX<0:
            self.bX=800
        if self.bY<0:
            self.bY=600
        screen.blit(self.birdImage, (self.bX, self.bY))


running=True
a=[0]*20
b=[bird() for i in a]
for i in range(20):
    a[i]=random.randint(0,359)
while (running):
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    for i in range(20):
        b[i].updateOrientation(a[i])

    pygame.display.update()