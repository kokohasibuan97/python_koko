def sum_then_print(message, *numbers, suffix_message): 
    total = 0
    for n in numbers: 
        total = total + n
    print(f"{message} {total} {suffix_message}")

sum_then_print("total nilai:", 2, 3, 4, 5, 4, suffix_message="selesai!") 