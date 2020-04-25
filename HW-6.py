# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:35:38 2020

@author: eason
"""

class pet():
    def __init__(self,name,width,height):
        self.name=name
        self.width=width
        self.height=height
    def LEGS(self):
        return self.width / ((self.height/50)*20)
a = pet("Just Pet",50,100)
print(a.name,a.LEGS())
class cat(pet):
    def __init__(self,clean,fat,angry):
        super.__init__()
        self.clean=clean
        self.fat=fat
        self.angry=angry
class dog(pet):
    def __init__(self,soft,play,happy):
        super.__init__()
        self.soft-soft
        self.play=play
        self.happy=happy