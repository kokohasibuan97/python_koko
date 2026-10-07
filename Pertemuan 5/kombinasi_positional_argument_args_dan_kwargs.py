def print_all(message, *params, **others): 
    print(f"message: {message}") 
    print(f"params: {params}") 
    print(f"others: {others}")

print_all("hello world", 1, True, ("yesn't", "nope"), name="nokia 3310", discontinued=True, year_released=2000)
