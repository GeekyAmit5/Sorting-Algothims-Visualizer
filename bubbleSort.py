import random
import pygame
import time


def bubbleSort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                pygame.draw.line(win, black, (10+i, 550), (10+i, 550-l[i]))
                l[i], l[j] = l[j], l[i]
                pygame.draw.line(win, random.choice(colors),
                                 (10+j, 550), (10+j, 550-l[j]))
                pygame.draw.line(win, random.choice(colors),
                                 (10+i, 550), (10+i, 550-l[i]))
                pygame.display.update()


pygame.init()
width = 1300
height = 600
pygame.display.set_caption("Bubble Sort")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [red, white, yellow, green, blue]
list = [random.randint(1, 500) for x in range(1280)]
for i in range(len(list)):
    pygame.draw.line(win, random.choice(colors),
                     (10+i, 550), (10+i, 550-list[i]))
pygame.display.update()
time.sleep(1)
bubbleSort(list)
print(list)
time.sleep(1)
