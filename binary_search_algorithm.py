#coding:utf-8
import time
start = time.time()
liste = [1,2,3,4,5,6,7,8,9]
try:
    value = int(input("1 ile 9 arasinda deger giriniz: "))
    middle = 0
    counter = 1
    while True:
        middle = liste[int(len(liste)/2)]
        if value > middle and len(liste) != 1:
            counter += 1
            liste = liste[liste.index(middle):]
            continue
        elif value < middle and len(liste) != 1:
            counter += 1
            liste = liste[:liste.index(middle)]
            continue
        elif value == middle:
            print(counter,"Defada bulundu")
            break
        else:
            print("Hatali islem")
            break
except Exception as exception:
    print(exception)
end = time.time()
print("Bu algoritma ile",end-start,"ms surdu bu isleminiz...")
