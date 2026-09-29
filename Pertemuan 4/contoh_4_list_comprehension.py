list_x = ['a','b','c']
list_y = ['1','2','3']

seq = []
for x in list_x:
    for y in list_y:
        seq.append(x+y)
print(seq)

#versi ringkas
seq = [x+y for x in list_x for y in list_y]
print(seq)