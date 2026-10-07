def print_data(**data): 
    print(f"type: {type(data)}")
    print(f"data: {data}")

    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data(phone="nokia 3310", discontinue=False, year=2000,networks=["GSM", "TDMA"])
