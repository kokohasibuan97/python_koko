fellowship = {'aragorn','gimli','legolas','gandalf','boromir','frodo','sam','merry','pippin'}

hobbits_1 = {'frodo','sam','merry','pippin','bilbo'}
res_1 = fellowship.issuperset(hobbits_1)
print("res_1:",res_1)

hobbits_2 = {'frodo','sam','merry','pippin'}
res_2 = fellowship.issuperset(hobbits_2)