#coding:utf-8
def takecube(number):
    return number*number*number

numbers = range(10)
print(list(map(takecube,numbers)))

#print(list(map(lambda x: x ** 2,(range(10))))) #map ve lambda ile 10 a kadar kare alma
