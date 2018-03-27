#coding:utf-8
import time

start = time.time()
folder = open("odev.txt","r")
rows = folder.readlines()
Upieces = {"sodaAdet":0,"sutAdet":0,"peynirAdet":0,"ekmekAdet":0,"suAdet":0}
Cpieces = {"sodaAdet":0,"sutAdet":0,"peynirAdet":0,"ekmekAdet":0,"suAdet":0}
Hpieces = {"sodaAdet":0,"sutAdet":0,"peynirAdet":0,"ekmekAdet":0,"suAdet":0}
def calculate(pieces):
    objectes = data[1].split(" ")[:-1]
    i = 0
    while i < len(objectes):
        if objectes[i].split(":")[0] == "soda":
            pieces["sodaAdet"] += int(objectes[i].split(":")[1])
        if objectes[i].split(":")[0] == "sut":
            pieces["sutAdet"] += int(objectes[i].split(":")[1])
        if objectes[i].split(":")[0] == "peynir":
            pieces["peynirAdet"] += int(objectes[i].split(":")[1])
        if objectes[i].split(":")[0] == "ekmek":
            pieces["ekmekAdet"] += int(objectes[i].split(":")[1])
        if objectes[i].split(":")[0] == "su":
            pieces["suAdet"] += int(objectes[i].split(":")[1])
        i += 1
    return pieces
for line in rows:
    data = line.split("=>")
    coordinate = data[0]
    if coordinate == "universite ":
        Upieces = calculate(Upieces)
    elif coordinate == "hastane ":
        Hpieces = calculate(Hpieces)
    elif coordinate == "merkez ":
        Cpieces = calculate(Cpieces)
print("Üniversite => ",Upieces)
print("Merkez => ",Cpieces)
print("Hastane => ",Hpieces)

for i in Upieces.keys():
    print(i,Upieces[i]+Cpieces[i]+Hpieces[i])
end = time.time()
print(end-start,"ms")
folder.close()
