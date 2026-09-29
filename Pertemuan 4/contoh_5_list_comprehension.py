matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

transposed = []
for i in range(4):
    tr = []
    for row in matrix:
        tr.append(row[i])
    transposed.append(tr)
print(transposed)

#versi ringkas
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

transposed = [[row[i] for row in matrix] for  i in range(4)]
print(transposed)