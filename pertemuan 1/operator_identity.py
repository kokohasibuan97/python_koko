#Operator identity

num_1= 100001
num_2= 100001

res= num_1 is num_2
print("num_1 is num_2=", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))