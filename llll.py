# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:10:59 2020

@author: eason
"""

"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame

# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
PINK     = ( 255,   0, 255)
# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("我的遊戲")

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()

# -------- 主要的程式迴圈 -----------
x=0
y=0
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = False # 將done變數設為True-->while迴圈將會結束
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= 1
    elif  keys[pygame.K_RIGHT]:
        x += 1
    elif  keys[pygame.K_UP]:
        y -= 1
    elif  keys[pygame.K_DOWN]:
        y += 1
    else:
        pass
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [x +10, y +10, 10 ,10])
    pygame.display.flip()
    # --- 程式的運算與邏輯
    

    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉

    # --- 每秒鐘60個frame
    clock.tick(60)

# 關閉式窗並離開程式
pygame.quit()







