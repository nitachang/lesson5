# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:36:01 2021

@author: nitac
"""

for x in [1,2,3,4]:
    print(x)
    
print('---------------')
    
ex=[1,'dog',2.5]
for z in ex:
    print(z)

print('---------------')

mylist=[]
mylist.append(1)
print(mylist)
mylist.append('dog')
print(mylist)
mylist.append(1.6)
print(mylist)

print('---------------')


mylist=[]
z=0
while z<1:
    x=input('需要的東西?')
    mylist.append(x)
    z=z+1
print(mylist)

print('---------------')

score=[]
x=int(input('學生人數?'))
for i in range(x):
    y=int(input('成績?'))
    score.append(y)
    
print(score)

print('---------------')

score=[]
x=int(input('學生人數?'))
g=0
for i in range(x):
    y=int(input('數學成績?'))
    score.append(y)
    g=g+y    
print(score)
print(float(g//x))

















    
    



