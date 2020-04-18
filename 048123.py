# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:32:33 2020

@author: eason
"""

class Human():
    def __init__(self,name,width,height):
        self.name=name
        self.width=width
        self.height=height
    def BMI(self):
        return self.width / ((self.height/100)**2)
a = Human("JoJO",50,150)
print(a.name,a.BMI())