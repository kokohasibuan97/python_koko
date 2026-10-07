#fungsi str
number = 24
string1 = str(number)
print(string1)

#string formatting
number = 24
string1 = f"{number}"
print(string1)

items = [1,2,3,4]
string2 = f"{(items)}"
print(string2)

obj = {
    "name":"AMD Ryzen 500g",
    "type":"processor",
    "igpu":True,
}
string3 = f"{obj}"
print(string3)