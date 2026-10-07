def outer_func(numbers = []): 
    print(f"numbers: {numbers}")

    def inner_func():
        print(f"max: {max(numbers)}")


print("call outer_func()") 
numbers = [1, 2, 3, 4] 
print(f"numbers: {numbers}")

print("call inner_func() within outer_func()") 
print(f"max: {max(numbers)}")
print(f"min: {min(numbers)}")

print("call inner_func() outside of outer_func()") 
print(f"max: {max(numbers)}")
print(f"min: {min(numbers)}")
