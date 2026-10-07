def print_data(message, number, **data): 
    print(f"message: {message}") 
    print(f"number: {number}")
    print()
    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data("sesuk prei", 2023, phone="nokia 3315", networks=["GSM", "TDMA"])
