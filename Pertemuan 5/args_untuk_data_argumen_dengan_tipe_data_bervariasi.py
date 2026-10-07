def print_data(*params):
    print(f"type: {type(params)}, data: {params}") 
    for i in range(len(params)):
        print(f"param {i}: {params[i]}")

print_data("hello python", 123, [5, True, ("yesn't")], {"iwak", "peyek"}) 