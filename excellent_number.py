#coding:utf-8
excellent = int(input("Sayı Giriniz: "))
dividing = ""
for i in range(1,int(excellent)):
    if int(excellent) % i == 0:
        dividing += str(i)
total = 0
for j in range (len(dividing)):
    total += int(dividing[j])
if total == excellent:
    print(True)
else:
    print(False)
