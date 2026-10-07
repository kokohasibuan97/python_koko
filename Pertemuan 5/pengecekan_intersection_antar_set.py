fellowship = {'aragorn','gimli','legolas','gandalf','boromir','frodo','sam','merry','pippin'}
hobbits = {'frodo','sam','merry','pippin','bilbo'}

fellowship.intersection_update(hobbits)
print("fellowship:",fellowship)