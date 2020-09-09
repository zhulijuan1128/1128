# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:10:43 2020

@author: tute
"""

#class_student.py
class Student:
   def __init__(self,name,age):
       self.name=name
       self.__age=age
    
   def say(self):
        return self.name
    
   def getage(self):
        return self.__age
    
           
su=Student('易烊千玺',20)
print(su.say())
print(su.getage())
print("大家好，我是",su.say(),"年龄：",su.getage())
    
