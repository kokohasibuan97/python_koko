def format_data(data):
    if data is not None:
        print(f"data: {data}")
    else:
        print("no data")

format_data("hello")
format_data(None)