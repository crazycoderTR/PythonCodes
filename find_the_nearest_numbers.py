#coding:utf-8
import random
numbers = []

for i in range (100):
    numbers.append(random.random())
numbers.sort()
val1 = 0
val2 = 0
smallest = 100
for i in range (len(numbers)-1):
    if smallest > abs(numbers[i]-numbers[i+1]):
        smallest = abs(numbers[i]-numbers[i+1])
        val1 = numbers[i]
        val2 = numbers[i+1]
print("Çekilen sayılar arasında birbirine en yakın iki sayı: ",float(val1)," - ",float(val2))
