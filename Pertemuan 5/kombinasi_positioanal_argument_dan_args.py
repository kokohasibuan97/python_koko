def sum_then_print(message, *numbers): 
    total = 0
    for n in numbers: 
        total = total + n
    print(f"{message} {total}")

sum_then_print("total nilai:", 2, 3, 4, 5, 4) 