#coding:utf-8
def oddnumber(number):
    return number%2 == 1

numbers = range(10)
print(list(filter(oddnumber,numbers)))
