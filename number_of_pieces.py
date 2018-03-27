#coding:utf-8
import random
import string 

data = {}
values = []
for i in range (100):
    values.append(random.randint(1,9))
for i in range (1,10):
    data[i] = values.count(i)
print("Sözlük ",data)
