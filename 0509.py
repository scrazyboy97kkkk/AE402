# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:34:22 2020

@author: eason
"""
import pygame,math
class Ball(pygame.sprite.Sprite):
    dx=0
    dy=0
    x=0
    y=0
    def __init__(self, speed, srx, sry, radium, color):
       
        pygame.sprite,Sprite.__init__(self)
        self.x=srx
        self.y=sry
        radium=math.radians(direction) 
        def update(self):
            self.x +=self.dx
            self.y +=self.dy
            self.rect.x= self.x
            self.rect.y= self.y