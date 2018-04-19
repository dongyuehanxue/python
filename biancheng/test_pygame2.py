#-*- coding=utf-8 -*-
import pygame,sys,random,math
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

# =============不同矩形==============
# for i in range(100):
#     width = random.randint(0,500)
#     height = random.randint(0,300)
#     top = random.randint(0,400)
#     left = random.randint(0,100)
#     color_name = random.choice(THECOLORS.keys())
#     color = THECOLORS[color_name]
#     pygame.draw.rect(screen,color,[left,top,width,height],1)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# ==========正弦曲线==============
# for x in range(0,640):
#     y = int(math.sin(x/640.0*4*math.pi)*200+240)
#     pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# ============正弦曲线2==========
# 连接多个点 参数：画线的表面；颜色；是否画一条线将最后一个点与第一个点相连接，使形状闭合；连接点的列表；线宽
#创建点列表
# plotPoints = []
# for x in range(0,640):
#     y = int(math.sin(x/640.0*4*math.pi)*200+240)
#     plotPoints.append([x,y])
# pygame.draw.lines(screen,[0,0,0],False,plotPoints,2)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()


# # =============连接多个点=================
# dots = [[221,432],[225,331],[133,342],[141,310],
#         [51,230],[74,217],[58,153],[114,164],
#         [123,135],[176,190],[159,77],[193,93],
#         [230,28],[267,93],[301,77],[284,190],
#         [327,135],[336,164],[402,153],[386,217],
#         [409,230],[319,310],[327,342],[233,331],[237,432]]

# pygame.draw.lines(screen,[255,0,0],True,dots,2)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# ===============引入图片========================
# my_ball = pygame.image.load("ball.png")
# screen.blit(my_ball,[100,100])

# # 动起来
# pygame.time.delay(2000)
# screen.blit(my_ball,[150,100])

# # 原来的图像覆盖
# pygame.draw.rect(screen,[255,255,255],[100,100,200,200],0)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# ================流畅的移动==============================
my_ball = 