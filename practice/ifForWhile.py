#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年12月8日
python条件控制语句
@author: chenshuai
'''

#if elif else
age = 3

if age > 5:
    print 'age more than 5'
elif age > 0 and age <= 5 :
    print 'age less then 5'
else :
    print 'age is ileagle'

# for
list1 = [1,2,3,4,5,6,7]
sumucoin = 0 
for x in list1:
    sumucoin = sumucoin + x
print sumucoin

#获取索引
for index in range(len(list1)):
    print list1[index]

# while
acount = 10;
while acount > 0:
    acount = acount - 1;

print acount
    


