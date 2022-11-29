#quicksort

from random import shuffle
import pygame, time
from math import ceil
from random import shuffle
import pygame, time
sizex = 1800    
sizey = 1200
surface = pygame.display.set_mode((sizex,sizey))
colour = [255, 5, 5]
black = (0,0,0)
red = (255, 5, 5)
black = (0,0,0)
green = (0, 255, 5)
blue = (5, 5, 255)

n = 1200
nums = [x for x in range(1, n+1)]
shuffle(nums)

delay = 0.00001

def draw_shapes(nums, position, colour): #draw the list
    pygame.draw.rect(surface, black, pygame.Rect(ceil(position*(sizex/n)), 0, ceil(len(nums)*sizex/n), sizey))
    pygame.display.update()
    for i in range(len(nums)):
        time.sleep(delay)
        pygame.draw.rect(surface, colour, pygame.Rect(ceil(position*(sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n))))
        pygame.display.update(ceil(position*(sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n)))


def quick_sort(nums, pos):
    time.sleep(delay)
    draw_shapes(nums, pos, red)
    if len(nums) == 0:
        draw_shapes(nums, pos, blue)
        return nums

    #pivot
    pivot = nums[-1]
    l = []
    r = []

    for num in nums[:-1]:
        if num <= pivot:
            l.append(num)
        if num > pivot:
            r.append(num)
    
            
    l = quick_sort(l, pos)
    r = quick_sort(r, pos+len(l))
    #reasembly

    nums = [l, [pivot], r]
    nums = [item for elem in nums for item in elem]
    draw_shapes(nums, pos, red)
    return nums
draw_shapes(nums, 0, red)
nums = quick_sort(nums, 0,)
for i in range(len(nums)):
        time.sleep(delay/2)
        pygame.draw.rect(surface, green, pygame.Rect(ceil((sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n))))
        pygame.display.update(ceil((sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n)))


running = True
while running:  
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            running = False