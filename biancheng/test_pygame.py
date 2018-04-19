import pygame
pygame.init()
from pygame.color import THECOLORS
# 建立一个窗口，大小
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255]) #用白色填充窗口
 #画一个圆 参数：在那个表面画圆（screen）；颜色（255,255,0）；位置（100,100）；
 # 大小（30，半径）；线宽（0为填充）
# pygame.draw.circle(screen,[255,0,0],[100,100],30,0) 
# pygame.draw.circle(screen,THECOLORS["blue"],[100,200],30,0)

# 矩形  (left,top,width,height)
pygame.draw.rect(screen,[255,255,0],[200,200,200,150],2)
pygame.display.flip()
running = True
# 改窗口在用户尝试关闭时关闭
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()