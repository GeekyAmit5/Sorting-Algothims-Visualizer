import random
import pygame
import time


def insertionSort(l):
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            pygame.draw.line(win, black, (9+j, 550), (9+j, 550-l[j-1]))
            l[j], l[j-1] = l[j-1], l[j]
            pygame.draw.line(win, random.choice(colors),
                             (9+j, 550), (9+j, 550-l[j-1]))
            pygame.draw.line(win, random.choice(colors),
                             (10+j, 550), (10+j, 550-l[j]))
            pygame.display.update()
            j -= 1


pygame.init()
width = 1300
height = 600
pygame.display.set_caption("insertion Sort")
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
insertionSort(list)
print(list)
time.sleep(1)
