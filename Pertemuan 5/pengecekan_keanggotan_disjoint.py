fellowship = {'aragorn','gimli','legolas','gandalf','boromir','frodo','sam','merry','pippin'}

res_1 = fellowship.isdisjoint(('aragorn','gimli'))
print("res_1:",res_1)

res_2 = fellowship.isdisjoint(('pippin','bilbo'))
print("res_2:",res_2)

res_3 = fellowship.isdisjoint(('bilbo'))
print("res_3:",res_3)

