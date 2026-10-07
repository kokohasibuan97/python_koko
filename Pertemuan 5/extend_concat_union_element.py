hobbits = {'frodo','sam','marry','pippin'}
dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimli'}
human = {'boromir'}
maiar = {'gandalf'}

#via union
fellowship_1 = hobbits.union(dunedain).union(elf).union(dwarf).union(human).union(maiar)
print("fellowship_1:",fellowship_1)

#via hobbits
hobbits = {'frodo','sam','merry','pippin'}
print(hobbits)