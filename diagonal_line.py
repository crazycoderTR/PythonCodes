#coding:utf-8
matrix = []
for i in range (5):
    matrix += [[0]*5]
for i in range (1,4):
    matrix[i][i] = 1
for i in range(5):
    print(matrix[i])
