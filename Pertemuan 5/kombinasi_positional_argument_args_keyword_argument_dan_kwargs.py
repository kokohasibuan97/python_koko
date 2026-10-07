def print_all(message, *params, say_something, **others): 
    print(f"message: {message}")
    print(f"params: {params}") 
    print(f"say_something: {say_something}") 
    print(f"others: {others}")

print_all("hello world", 1, True, ("yesn't", "nope"), say_something="how are you", name="nokia 3310", discontinued=True, year_released=2000)
