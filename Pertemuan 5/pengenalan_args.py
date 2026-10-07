def sum_then_print(n1, n2, n3, n4, n5): 
    total = n1 + n2 + n3 + n4 + n5 
    print(total)

sum_then_print(2, 3, 4, 5, 4) 

def sum_then_print(*numbers): 
    total = 0
    for n in numbers: 
        total = total + n
    print(total)

sum_then_print(2, 3, 4, 5, 4) 