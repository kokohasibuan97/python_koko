message1 = "hello world" 
message2 = message1 
message3 = "hello world"

print(f"message1 ({id(message1)}) is message2 ({id(message2)}) ➜ {message1 is message2}")
print(f"message1 ({id(message1)}) is message3 ({id(message3)}) ➜ {message1 is message3}")
print(f"message2 ({id(message2)}) is message3 ({id(message3)}) ➜ {message2 is message3}") 

message2 = "hello world"
print(f"message1 ({id(message1)}) is message2 ({id(message2)}) ➜ {message1 is message2}")


#fase 1
message1 = "hello world"
message2 = message1 
message3 = "hello world"

 #fase 2
message1 = "hello world" 
message2 = message1
message3 = "hello world"

message2 = "hello world"

#fase 3
message1 = "hello world"
message2 = message1 
message3 = "hello world"

message2 = "hello world"

message3 = message2

