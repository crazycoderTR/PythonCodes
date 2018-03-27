#coding:utf-8
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[9,8,7],[6,5,4],[3,2,1]]
m3 = [[0,0,0],[0,0,0],[0,0,0]]
i = 0
m = 0
k = 0
l = 0
while i < len(m1)*len(m2):
    total = 0
    for s in range(len(m2)):
        total += m1[k][s] * m2[s][m]
    m += 1
    m3[k][l] = total
    l += 1
    if i == 2 or i == 5 or i == 8:
        k +=1
        l = 0
        m = 0
    i += 1
print(m3)
