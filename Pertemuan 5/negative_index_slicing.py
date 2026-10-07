data_str = "hello world" 
print(data_str[-1])

print(data_str[-5]) 

data_str = "hello world"

# slicing 3 karakter terakhir 
slice1 = data_str[-3:] 
print(slice1)

# slicing dari index -5 hingga -2 
slice2 = data_str[-5:-2] 
print(slice2)

# slicing dengan step negatif (reverse) 
slice3 = data_str[::-1]
print(slice3)

data_list = [2, 4, 6, 7, 9, 11, 13]

# dari index 1 hingga 2 element terakhir 
list1 = data_list[1:-2]
print(list1)

# 3 element terakhir 
list2 = data_list[-3:] 
print(list2)

# seluruh element kecuali 2 terakhir 
list3 = data_list[:-2]
print(list3)

# reverse list
list4 = data_list[::-1] 
print(list4)
