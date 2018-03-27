#coding:utf-8
with open("deneme.txt","r") as dosya:
    a = dosya.read()
    print(a)

dosya.seek(0)
a = dosya.read()
print(a)

with open("deneme.txt","r+") as dosya:
    veri = dosya.read()
    dosya.seek(0)
    dosya.write("ekleme ekleme ekleme"+veri)

with open("deneme.txt","r+") as dosya:
    veri = dosya.readlines()
    veri.insert(2,"bu da ekleme hııaaammıınaa")
    veri.seek(0)
    dosya.writelines(veri)
