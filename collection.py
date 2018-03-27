#coding:utf-8
import sys
numbers = 0
def collection(*numbers):
    total = 0
    for i in numbers:
        total += int(i)
    return total
for i in range(1,len(sys.argv)):
    numbers += int(sys.argv[i])
print("sonuc: ",collection(numbers))
