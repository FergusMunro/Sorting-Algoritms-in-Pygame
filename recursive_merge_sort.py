#recursive merge sort
#please fucking work

from math import ceil
from random import shuffle
import pygame, time
sizex = 1800    
sizey = 1200
surface = pygame.display.set_mode((sizex,sizey))
red = (255, 5, 5)
black = (0,0,0)
green = (0, 255, 5)
blue = (5, 5, 255)


n = 2048
delay = 0.0005
nums = [x for x in range(1, n+1)]
shuffle(nums)


def draw_shapes(nums, position, colour): #draw the list
    pygame.draw.rect(surface, black, pygame.Rect(ceil(position*(sizex/n)), 0, ceil(len(nums)*sizex/n), sizey))
    pygame.display.update()
    for i in range(len(nums)):
        time.sleep(delay)
        pygame.draw.rect(surface, colour, pygame.Rect(ceil(position*(sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n))))
        pygame.display.update(ceil(position*(sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n)))


def merge(nums1, nums2):
    nums = []
    flag = True
    while flag:
        try:
            if nums1[0] < nums2[0]:
                nums.append(nums1[0])
                nums1.pop(0)
            else:
                nums.append(nums2[0])
                nums2.pop(0)
        except IndexError:
            flag = False
            if len(nums1) != 0:
                for item in nums1:
                    nums.append(item)
            elif len(nums2) != 0:
                for item in nums2:
                    nums.append(item)
    return nums  

def merge_sort(nums, pos):
    if len(nums) == 1:
        draw_shapes(nums, pos, blue)
        return nums

    half = ceil(len(nums)/2)
    l = merge_sort(nums[half:], pos)
    r = merge_sort(nums[:half], pos + half)

    #merge the lists

    nums = merge(l, r)
    draw_shapes(nums, pos, red)
    return nums

draw_shapes(nums, 0, red)
nums = merge_sort(nums, 0)
for i in range(len(nums)):
        time.sleep(delay/2)
        pygame.draw.rect(surface, green, pygame.Rect(ceil((sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n))))
        pygame.display.update(ceil((sizex/n)) + ceil(i*(sizex/n)), sizey-ceil((nums[i])*(sizey/n)), ceil(sizex/n), ceil((nums[i])*(sizey/n)))


running = True
while running:  
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            running = False
