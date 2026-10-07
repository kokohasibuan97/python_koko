def aggregate(message, numbers, f): 
    res = f(numbers) 
    print(f"{message} is {res}")