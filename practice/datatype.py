#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年12月8日
python为动态语言，变量本身类型不固定
@author: chenshuai
'''

#整形
youcoin = 10
print youcoin, int('100')

#字符串
mystr = "str"
print mystr, mystr.__len__(), len(mystr), mystr.upper(),mystr.title()

#布尔值
isRitht = True
print isRitht,False, 10 > 3, not True

#控制
nu=None
print nu

#list 可变有序列表
names = ['chenshuai','renjia','xiaoyu','xiaoshuai']
names.append("xiaoxue")
print names[0],names[-1],len(names)
names.sort()
print names

#tuple 不可变有序列表
ages = (10,20,5,46)
oneTuple = (1,)
print ages[0],ages[-2],len(ages), oneTuple

#dict 字典 相当于Map
student = {'name':'chenshuai', 'age':30}
student['gender'] = 1
print student, student.get('name'), student.has_key('sex'), student.get('sex', 1)

# set 不可重复无序集合
keySet = set([1, 2, 1, 1, 3, 5, 7, 7, 8, 9, 9, 9, 9])
print keySet, type(keySet)

set1 = set([1, 2, 3])
set2 = set([3, 4, 5])

print set1 & set2
print set1 | set2
